from itertools import groupby

from django.contrib import messages
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.forms import Select
from django.http import HttpResponseRedirect
from django.shortcuts import render

from admin.salesforce import check_dni_salesforce
from admin.utils import is_active_module
from associate.models import Associate
from candidatures.forms import NewCandidatureForm, NewCandidatureConfirmForm, NewCandidature15Form
from candidatures.models import Candidature
from circumscription.models import Circumscription


def presentation(request, _type):
    if not is_active_module(request, 'presentacion_%s' % _type) and not request.user.is_superuser:
        return HttpResponseRedirect('/')
    if _type == 60:
        form = NewCandidatureForm
        member = 'Socias/os'
    else:
        form = NewCandidature15Form
        member = 'Consejeras/os'
    if request.method == 'POST':
        form = form(request.POST, request.FILES)
        if form.is_valid():
            if not check_dni_salesforce(request.POST.get('dni_number')):
                message = 'El DNI introducido no corresponde a ningún socio en activo, se puede actualizar en ' \
                          'la WEB de Greenpeace en Mi Perfil https://miperfil.greenpeace.es/'
                messages.add_message(request, messages.WARNING, message)
                return render(request, 'presentation.html', {'form': form})

            if Candidature.objects.filter(dni_number=request.POST.get('dni_number'), announcement=_type).count() > 0:
                message = 'Ya hay una candidatura registrada con este DNI'
                messages.add_message(request, messages.ERROR, message)
                return render(request, 'presentation.html', {'form': form})
            candidate = form.save(commit=False)
            if _type == 15:
                candidate.circumscription_id = 19
            candidate.save()
            request.session['candidate_id'] = candidate.id
            return HttpResponseRedirect(f'confirmar_{_type}')
    return render(request, 'presentation.html', {'form': form, 'member': member})


def confirm(request, _type):
    if not is_active_module(request, 'presentacion_%s' % _type) and not request.user.is_superuser:
        return HttpResponseRedirect('/')
    candidate = Candidature.objects.get(pk=request.session['candidate_id'])
    if request.method == 'POST':  # If the form has been submitted...
        candidate.announcement = _type
        candidate.partner_number = 'n/a'
        candidate.save()
        envia_confirmacion(candidate)
        return HttpResponseRedirect(f'/ok_{_type}')
    else:
        form = NewCandidatureConfirmForm(instance=candidate)
        c = dict(form=form, candidate=candidate)
        for k in form.fields:
            w = form.fields[k].widget
            if isinstance(w, Select):
                w.attrs['disabled'] = True
            else:
                w.attrs['readonly'] = True

        return render(request, 'presentation_preview.html', c)


def envia_confirmacion(candidato):
    form = NewCandidatureConfirmForm(instance=candidato)
    ret = u'Se ha recibido la siguiente candidatura al Consejo de Greenpeace España:\n'
    for f in form:
        if f.name == 'circumscription':
            ret += '\n%s: %s' % (f.label, Circumscription.objects.get(pk=f.value()))
        else:
            ret += '\n%s: %s' % (f.label, f.value())
    ret += u'\nSi lo consideras necesario, contacta con la Comisión Electoral en eleccion.es@greenpeace.org.\nGracias'
    destinatarios = [form['email'].value()]
    eles = get_user_model().objects.filter(username='eles').first()
    if eles:
        destinatarios.append(eles.email)
    # if candidato.presenta and candidato.presenta.correo_electronico:
    #     destinatarios.append(candidato.presenta.correo_electronico)
    send_mail(
        subject=u"Candidatura al Consejo de Greenpeace España", message=ret, from_email='eleccion.es@greenpeace.org',
        recipient_list=destinatarios,
    )


def allegation(request, _type):
    if not is_active_module(request, 'alegaciones_%s' % _type) and not request.user.is_superuser:
        return HttpResponseRedirect('/')
    candidate = Candidature.objects.filter(announcement=_type)
    valid_candidate = candidate.filter(validated=True).order_by('circumscription', 'seniority_date')
    not_valid_candidate = candidate.exclude(validated=True).order_by('lastname', 'firstname')

    ccaa = [(k, list(v)) for (k, v) in groupby(valid_candidate, lambda x: x.circumscription)]
    context = {'ccaa': ccaa, 'not_valid_candidate': not_valid_candidate}
    return render(request, 'allegations.html', context=context)


def view_candidatures(request, _type):
    if not is_active_module(request, 'ver_candidaturas_%s' % _type) and not request.user.is_superuser:
        return HttpResponseRedirect('/')
    candidates = Candidature.objects.filter(announcement=_type)
    valid_candidates = candidates.filter(validated=True).order_by('circumscription', 'seniority_date')
    ccaa = [(k, list(v)) for (k, v) in groupby(valid_candidates, lambda x: x.circumscription)]
    context = {'ccaa': ccaa}
    associate_id = request.session.get('associate_id')
    if associate_id:
        member = Associate.objects.get(pk=associate_id)
        member_circ = valid_candidates.filter(circumscription=member.circumscription)
        context['member_circ'] = member_circ
        request.session.pop('associate_id')
    return render(request, 'view_candidatures.html', context=context)


def send_allegation_mail(candidate, msg, email):
    ret = f'Se ha realizado una alegación al candidato: {candidate}\n'
    ret += f'\n{msg}\nGracias'
    eles = get_user_model().objects.filter(username='eles').first()
    if eles:
        destinatarios = [eles.email, email]
        send_mail(
            subject=u"Se ha generado una alegación", message=ret, from_email='eleccion.es@greenpeace.org',
            recipient_list=destinatarios,
        )