from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'content']
        widgets = {
            'rating': forms.RadioSelect(choices=[(True, 'I like it'), (False, "I don't like it")]),
            'content': forms.Textarea(attrs={'rows': 4, 'cols': 15, 'placeholder': 'Your Review...'}),
        }