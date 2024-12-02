from django import forms

class ReviewForm(forms.Form):
    user_name = forms.CharField(label="Your name",required=True, error_messages={
        "required":"Your name is required!"
    })
    texfield= forms.CharField(widget=forms.Textarea, label="Your feedback")
    review = forms.IntegerField(max_value=5,min_value=1)
    