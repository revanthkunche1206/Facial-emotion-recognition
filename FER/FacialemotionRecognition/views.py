from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .FERmodel import predict_emotion

@csrf_exempt
def detect_emotion(request):
    if request.method == 'POST':
        image_data = request.FILES['frame'].read()
        emotion_label = predict_emotion(image_data)
        return JsonResponse({'emotion': str(emotion_label)})

from django.shortcuts import render
def home(request):
    return render(request, 'home.html')
