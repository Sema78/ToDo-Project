from django import forms
from .models import ToDoItem


class ToDoItemForm(forms.ModelForm):

    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = ToDoItem
        fields = [
            'title',
            'description'
        ]
        exclude =('date_pub', 'completed',)