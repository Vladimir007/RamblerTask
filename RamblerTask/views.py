import os
import logging
from django.http import JsonResponse
from django.shortcuts import render
from RamblerTask.utils import Pickle


def calculate_pickle(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Only POST request is supported'})
    vals_arr = []
    required_vals = ['f1', 'f2', 'f3', 'f4']
    for x in required_vals:
        if x not in request.POST:
            return JsonResponse({'error': "Parameter '%s' is required" % x})
        try:
            vals_arr.append(float(request.POST[x]))
        except ValueError:
            return JsonResponse({'error': "Parameter '%s' must have float type" % x})
    try:
        res = Pickle().calc_pickle(vals_arr)
    except Exception as e:
        logger = logging.getLogger('RamblerTask')
        logger.exception("%s (Request parameters are: %s)" % (e, dict(zip(required_vals, vals_arr))), stack_info=True)
        return JsonResponse({'error': str(e)})
    return JsonResponse({'class': str(res)})


def change_pickle(request):
    if request.method != 'GET':
        return JsonResponse({'error': 'Only GET request is supported'})
    if 'pickle' not in request.GET:
        return JsonResponse({'error': "Please set 'pickle' GET parameter"})
    try:
        Pickle().set_new_pickle(request.GET['pickle'])
    except Exception as e:
        logger = logging.getLogger('RamblerTask')
        logger.exception(e)
        return JsonResponse({'error': str(e)})
    logger = logging.getLogger('RamblerTaskInfo')
    logger.info("Pickle file was changed to '%s'" % request.GET['pickle'])
    return JsonResponse({})


def index_page(request):
    return render(request, 'index.html', {
        'params': ['f1', 'f2', 'f3', 'f4'],
        'pickle': os.path.splitext(os.path.split(Pickle().get_pickle())[-1])[0]
    })
