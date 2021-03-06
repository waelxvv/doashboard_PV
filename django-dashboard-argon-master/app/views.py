# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django.http import JsonResponse


def supervision(request):

    labels = ['2019-02-01 08:00:00',
            '2019-02-01 09:00:00', 
            '2019-02-01 10:00:00',
            '2019-02-01 11:00:00',
            '2019-02-01 12:00:00',
            '2019-02-01 13:00:00',
            '2019-02-01 14:00:00',
            '2019-02-01 15:00:00',
            '2019-02-01 16:00:00',
            '2019-02-01 17:00:00',
            '2019-02-01 18:00:00',
            '2019-02-01 19:00:00',
            '2019-02-01 20:00:00',
            '2019-02-01 21:00:00',
            '2019-02-01 22:00:00',
            '2019-02-02 23:00:00',
            '2019-02-02 00:00:00',
            '2019-02-02 01:00:00',
            '2019-02-02 02:00:00',
            '2019-02-02 03:00:00',
            '2019-02-02 04:00:00',
            '2019-02-02 05:00:00',
            '2019-02-02 06:00:00',
            '2019-02-02 07:00:00',
            '2019-02-02 08:00:00',
            ]
    data = [1000,
            1100, 
            1200,
            1300,
            1500, 
            1600, 
            1660, 
            1400, 
            1200, 
            1100, 
            1200, 
            1500, 
            2000, 
            2500, 
            3000, 
            2800, 
            1000, 
            1000, 
            1000, 
            1000, 
            1000, 
            1000, 
            1300, 
            1350, 
            1500,]
    
    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })

def supervisionGrille(request):

    labels = ['2019-02-01 08:00:00',
            '2019-02-01 09:00:00', 
            '2019-02-01 10:00:00',
            '2019-02-01 11:00:00',
            '2019-02-01 12:00:00',
            '2019-02-01 13:00:00',
            '2019-02-01 14:00:00',
            '2019-02-01 15:00:00',
            '2019-02-01 16:00:00',
            '2019-02-01 17:00:00',
            '2019-02-01 18:00:00',
            '2019-02-01 19:00:00',
            '2019-02-01 20:00:00',
            '2019-02-01 21:00:00',
            '2019-02-01 22:00:00',
            '2019-02-02 23:00:00',
            '2019-02-02 00:00:00',
            '2019-02-02 01:00:00',
            '2019-02-02 02:00:00',
            '2019-02-02 03:00:00',
            '2019-02-02 04:00:00',
            '2019-02-02 05:00:00',
            '2019-02-02 06:00:00',
            '2019-02-02 07:00:00',
            '2019-02-02 08:00:00',
            ]
    data = [900,
            950, 
            1000,
            1100,
            1000, 
            1400, 
            1450, 
            1400, 
            1100, 
            1000, 
            1000, 
            1300, 
            1500, 
            2000, 
            10, 
            2600, 
            800, 
            800, 
            700, 
            500, 
            1000, 
            1000, 
            1100, 
            650, 
            1600,]

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })

def supervisionCharge(request):

    labels = ['2019-02-01 08:00:00',
            '2019-02-01 09:00:00', 
            '2019-02-01 10:00:00',
            '2019-02-01 11:00:00',
            '2019-02-01 12:00:00',
            '2019-02-01 13:00:00',
            '2019-02-01 14:00:00',
            '2019-02-01 15:00:00',
            '2019-02-01 16:00:00',
            '2019-02-01 17:00:00',
            '2019-02-01 18:00:00',
            '2019-02-01 19:00:00',
            '2019-02-01 20:00:00',
            '2019-02-01 21:00:00',
            '2019-02-01 22:00:00',
            '2019-02-02 23:00:00',
            '2019-02-02 00:00:00',
            '2019-02-02 01:00:00',
            '2019-02-02 02:00:00',
            '2019-02-02 03:00:00',
            '2019-02-02 04:00:00',
            '2019-02-02 05:00:00',
            '2019-02-02 06:00:00',
            '2019-02-02 07:00:00',
            '2019-02-02 08:00:00',
            ]
    data = [100,
            95, 
            100,
            100,
            100, 
            100, 
            50, 
            40, 
            50, 
            60, 
            70, 
            80, 
            90, 
            100, 
            100, 
            100, 
            100, 
            100, 
            100, 
            100, 
            100, 
            100, 
            100, 
            100, 
            100,]

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })

def supervisionConsommation(request):

    labels = ['2019-02-01 08:00:00',
            '2019-02-01 09:00:00', 
            '2019-02-01 10:00:00',
            '2019-02-01 11:00:00',
            '2019-02-01 12:00:00',
            '2019-02-01 13:00:00',
            '2019-02-01 14:00:00',
            '2019-02-01 15:00:00',
            '2019-02-01 16:00:00',
            '2019-02-01 17:00:00',
            '2019-02-01 18:00:00',
            '2019-02-01 19:00:00',
            '2019-02-01 20:00:00',
            '2019-02-01 21:00:00',
            '2019-02-01 22:00:00',
            '2019-02-02 23:00:00',
            '2019-02-02 00:00:00',
            '2019-02-02 01:00:00',
            '2019-02-02 02:00:00',
            '2019-02-02 03:00:00',
            '2019-02-02 04:00:00',
            '2019-02-02 05:00:00',
            '2019-02-02 06:00:00',
            '2019-02-02 07:00:00',
            '2019-02-02 08:00:00',
            ]
    data = [1000,
            1100, 
            1200,
            1300,
            1500, 
            1600, 
            1660, 
            1400, 
            1200, 
            1100, 
            1200, 
            1500, 
            2000, 
            2500, 
            3000, 
            2800, 
            1000, 
            1000, 
            1000, 
            1000, 
            1000, 
            1000, 
            1300, 
            1350, 
            1500,]
    
    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })


@login_required(login_url="/login/")
def index(request):
    return render(request, "index.html")

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]
        template = loader.get_template('pages/' + load_template)
        return HttpResponse(template.render(context, request))

    except:

        template = loader.get_template( 'pages/error-404.html' )
        return HttpResponse(template.render(context, request))
