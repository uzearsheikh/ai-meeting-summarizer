from django import forms

class MeetingForm(forms.Form):
    transcript = forms.CharField(
        widget=forms.Textarea,
        label="Meeting Transcript"
    )