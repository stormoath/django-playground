from django import forms
from .models import Note

class post_note(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('title','text','color')