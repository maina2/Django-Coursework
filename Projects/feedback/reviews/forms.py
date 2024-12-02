from django import forms
from .models import Review

# class ReviewForm(forms.Form):
#     user_name = forms.CharField(label="Your name",required=True, error_messages={
#         "required":"Your name is required!"
#     })
#     review_text= forms.CharField(widget=forms.Textarea, label="Your feedback")
#     rating = forms.IntegerField(max_value=5,min_value=1)
    
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'