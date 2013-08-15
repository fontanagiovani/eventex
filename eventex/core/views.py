# coding: utf-8
from datetime import time
from django.shortcuts import render, get_object_or_404
from eventex.core.models import Speaker, Talk


def homepage(request):
    return render(request, 'index.html')

def speaker_detail(request, slug):
    speaker = get_object_or_404(Speaker, slug=slug)
    contexto = {'speaker': speaker}
    return render(request, 'core/speaker_detail.html', contexto)

def talk_list(request):
    midday = time(12)
    context = {
        'morning_talks': Talk.objects.filter(start_time__lt=midday),
        'afternoon_talks': Talk.objects.filter(start_time__gte=midday)
    }
    return render(request, 'core/talk_list.html', context)