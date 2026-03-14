from django.shortcuts import render
from .transcribe import transcribe_audio
from .summarizer import generate_summary

def upload_meeting(request):

    summary = None

    if request.method == "POST":

        audio_file = request.FILES['audio']

        with open("meeting.wav", "wb") as f:
            for chunk in audio_file.chunks():
                f.write(chunk)

        transcript = transcribe_audio("meeting.wav")

        summary = generate_summary(transcript)

    return render(request,"index.html",{"summary":summary})

from django.shortcuts import render, redirect
from .models import Feedback



def index(request):
    feedbacks = []
    return render(request,"index.html",{"feedbacks":feedbacks})


def feedback(request):

    if request.method == "POST":

        name = request.POST.get("name")
        message = request.POST.get("message")
        rating = request.POST.get("rating")

        # agar 6 se zyada ho gaye to oldest delete
        if Feedback.objects.count() >= 6:
            Feedback.objects.first().delete()

        Feedback.objects.create(
            name=name,
            message=message,
            rating=rating
        )

        return redirect("/")

    return render(request, "feedback.html")