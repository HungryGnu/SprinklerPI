from django.shortcuts import render
from django.http import HttpResponse
from controler import models as cm
from controler.utils import sprinklerCycle
import RPi.GPIO as gpio
import json


# Set schedule and duration for zones:
def setZones(request):
    context_dict = {}
    content_type = 'application/json'
    if request.method == 'POST':
        pass
        # Clean the form data
        # if error return corrections
        # else no errors set db models and return success message
    elif request.method == 'GET':
        zone = request.GET.get('zone')
        zone = int(zone)
        try:
            cm.Zone.objects.get()
        # return the existing values in the db for a given zone
    else:
        context_dict['message'] = 'Only GET and POST HTTP requests are accepted by this endpoint'
        return HttpResponse(json.dumps(context_dict), content_type=content_type)

# Do an immediate run of a named zone:
def runNow(request):
    zone = request.GET.get('zone')
    all = request.GET.get('all')
    content_type = 'application/json'
    try:
        zone = int(zone)
        if all.lower()=='true' or '0':
            all = True
        else:
            all = False
        context_dict = {}
        # TODO: should intiate a task.  don't want to wait around for it.
        sprinklerCycle.run(all, zone)
        gpio.cleanup()
        context_dict['message'] = 'Task Submitted.'
        # HTTP response json data
    except ValueError:
        context_dict['message'] = 'Zone must be an integer.'
        # HTTPResponse json data
    return HttpResponse(json.dumps(context_dict), content_type=content_type)
    # Exception for not in Zone model?
