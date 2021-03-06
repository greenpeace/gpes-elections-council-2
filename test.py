import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")  # project_name nombre del proyecto
django.setup()

from circumscription.models import Circumscription

c = [
    {
        "pk": 1,
        "model": "comun.circunscripcion",
        "fields": {
            "orden": 5,
            "alize": "ANDALUCIA+CEUTA Y MELILLA",
            "ds": "Andaluc\u00eda, Ceuta y Melilla",
            "puestos": 3
        }
    },
    {
        "pk": 9,
        "model": "comun.circunscripcion",
        "fields": {
            "orden": 5,
            "alize": "Comunidad Aut\u00f3noma Vasca",
            "ds": "Comunidad Aut\u00f3noma Vasca",
            "puestos": 3
        }
    },
    {
        "pk": 4,
        "model": "comun.circunscripcion",
        "fields": {
            "orden": 10,
            "alize": "ARAGON",
            "ds": "Arag\u00f3n",
            "puestos": 1
        }
    },
    {
        "pk": 7,
        "model": "comun.circunscripcion",
        "fields": {
            "orden": 20,
            "alize": "Canarias",
            "ds": "Canarias",
            "puestos": 1
        }
    },
    {
        "pk": 10,
        "model": "comun.circunscripcion",
        "fields": {
            "orden": 30,
            "alize": "Cantabria",
            "ds": "Cantabria",
            "puestos": 1
        }
    },
    {
        "pk": 16,
        "model": "comun.circunscripcion",
        "fields": {
            "orden": 35,
            "alize": "Castilla-La Mancha",
            "ds": "Castilla-La Mancha",
            "puestos": 1
        }
    },
    {
        "pk": 13,
        "model": "comun.circunscripcion",
        "fields": {
            "orden": 40,
            "alize": "CASTILLA-LEON",
            "ds": "Castilla y Le\u00f3n",
            "puestos": 1
        }
    },
    {
        "pk": 2,
        "model": "comun.circunscripcion",
        "fields": {
            "orden": 60,
            "alize": "CATALU\u00d1A",
            "ds": "Catalu\u00f1a",
            "puestos": 11
        }
    },
    {
        "pk": 8,
        "model": "comun.circunscripcion",
        "fields": {
            "orden": 80,
            "alize": "Comunidad Foral de Navarra",
            "ds": "Comunidad Foral de Navarra",
            "puestos": 1
        }
    },
    {
        "pk": 11,
        "model": "comun.circunscripcion",
        "fields": {
            "orden": 90,
            "alize": "Comunidad Valenciana",
            "ds": "Comunidad Valenciana",
            "puestos": 7
        }
    },
    {
        "pk": 14,
        "model": "comun.circunscripcion",
        "fields": {
            "orden": 100,
            "alize": "Extremadura",
            "ds": "Extremadura",
            "puestos": 1
        }
    },
    {
        "pk": 17,
        "model": "comun.circunscripcion",
        "fields": {
            "orden": 110,
            "alize": "Galicia",
            "ds": "Galicia",
            "puestos": 2
        }
    },
    {
        "pk": 3,
        "model": "comun.circunscripcion",
        "fields": {
            "orden": 120,
            "alize": "ILLES BALEARS",
            "ds": "Islas Baleares",
            "puestos": 1
        }
    },
    {
        "pk": 6,
        "model": "comun.circunscripcion",
        "fields": {
            "orden": 130,
            "alize": "La Rioja",
            "ds": "La Rioja",
            "puestos": 1
        }
    },
    {
        "pk": 12,
        "model": "comun.circunscripcion",
        "fields": {
            "orden": 150,
            "alize": "Principado de Asturias",
            "ds": "Principado de Asturias",
            "puestos": 1
        }
    },
    {
        "pk": 15,
        "model": "comun.circunscripcion",
        "fields": {
            "orden": 160,
            "alize": "Regi\u00f3n de Murcia",
            "ds": "Regi\u00f3n de Murcia",
            "puestos": 1
        }
    },
    {
        "pk": 18,
        "model": "comun.circunscripcion",
        "fields": {
            "orden": 999,
            "alize": "n/a",
            "ds": "n/a",
            "puestos": 0
        }
    }
]

for x in c:
    _o = {
        'ds': x['fields']['ds'],
        'order': x['fields']['orden'],
        'alize': x['fields']['alize'],
        'places': x['fields']['puestos'],
    }
    Circumscription.objects.create(**_o)
