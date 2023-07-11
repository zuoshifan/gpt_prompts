from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Prompt

# Define a form class for creating a prompt
class PromptForm(forms.ModelForm):
    honeypot = forms.CharField(required=False, label=_('Leave this blank if you are a human'))

    # Meta class for form options
    class Meta:
        # Specify the model and the fields to be included in the form
        model = Prompt
        fields = ['title', 'category', 'cover', 'description', 'style', 'content', 'types', 'output', 'price_dollar', 'price_yuan']

        widgets = {
            'description': forms.Textarea(),
            'style': forms.RadioSelect(),
            'content': forms.Textarea(),
            'honeypot': forms.TextInput(
                attrs = {
                    'placeholder': _('If you enter anything in this field, your submit will be treated as spam.'),
                    'class': 'form-control'
                }
            ),
        }

    def clean_honeypot(self):
        """Check that nothing's been entered into the honeypot."""
        value = self.cleaned_data["honeypot"]
        if value:
            raise forms.ValidationError(self.fields["honeypot"].label)
        return value
