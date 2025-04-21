from django.shortcuts import render
from django.http import JsonResponse
import speech_recognition as sr
import tempfile
import os

# View to render the home page
def home(request):
    return render(request, 'index.html')

# View to process the uploaded audio and recognize speech
def process_audio(request):
    if request.method == 'POST' and request.FILES.get('audio'):
        audio_file = request.FILES['audio']

        # Save the uploaded audio file to a temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
            for chunk in audio_file.chunks():
                temp_audio.write(chunk)
            temp_audio_path = temp_audio.name

        recognizer = sr.Recognizer()
        try:
            # Process the audio file using the speech recognition library
            with sr.AudioFile(temp_audio_path) as source:
                audio = recognizer.record(source)
                text = recognizer.recognize_google(audio)
                print("Recognized Text:", text)
        except Exception as e:
            text = "Sorry, I couldn't understand that."
            print("Error:", e)
        finally:
            os.remove(temp_audio_path)

        # Return the recognized text as a JSON response
        return JsonResponse({'response': f"I heard you say: {text}"})

    return JsonResponse({'response': "No audio received."})

# Example additional views (you can add them as needed)
def dashboard(request):
    return render(request, 'dashboard.html')

def explainer(request):
    return render(request, 'explainer.html')

def ppt_maker(request):
    return render(request, 'ppt_maker.html')

def discussion(request):
    return render(request, 'discussion.html')

def quiz_builder(request):
    return render(request, 'quiz_builder.html')

def lesson_planner(request):
    return render(request, 'lesson_planner.html')
