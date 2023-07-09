from django import forms
from .models import ConversationMessage

class ConversationMessageForm(forms.ModelForm):
    class Meta:
        model = ConversationMessage
        fields = ('content',)
        labels = {
            'content': '',  # Remove the label for the 'content' field
        }
        widgets = {
            'content':forms.Textarea(attrs={
                'class':'w-full  p-2   rounded-3xl border',
                'rows':2,
                'cols':50,
                'placeholder':'Your text goes here...'
            })
        }