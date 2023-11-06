from django import forms
from .models import Review, Publishers, Developers, Tags

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'content']
        widgets = {
            'rating': forms.RadioSelect(choices=[(True, 'I like it'), (False, "I don't like it")]),
            'content': forms.Textarea(attrs={'rows': 4, 'cols': 15, 'placeholder': 'Your Review...'}),
        }

class SearchForm(forms.ModelForm):
    publisher = forms.ModelChoiceField(
        queryset=Publishers.object.all(),
        required=False
    )
    developer = forms.ModelChoiceField(
        queryset=Developers.objects.all(),
        required=False
    )
    tags = forms.ModelMultipleChoiceField(
        queryset=Tags.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple
    )