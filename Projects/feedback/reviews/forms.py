from django import forms

class ReviewForm(forms.Form):
    user_name = forms.CharField(label="Your name",required=True, error_messages={
        "required":"Your name is required!"
    })
