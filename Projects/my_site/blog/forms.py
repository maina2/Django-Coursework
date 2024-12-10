from .models import Comment
from django import forms


class CommentModelForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        exclude = ["post"]
        labels = {
            "user_name ":"Your name",
            "user_email":"Your email",
            "text":"Your comment"
        }
