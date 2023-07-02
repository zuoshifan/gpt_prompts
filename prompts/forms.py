# Import modules and functions
from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Template, Prompt

# Define a form for creating a template
class TemplateCreateForm(forms.ModelForm):
    # Meta class for form options
    class Meta:
        # Specify the model and fields for the form
        model = Template
        fields = ['title', 'content', 'category', 'language', 'price']

        # Specify the labels and placeholders for the fields
        labels = {
            'title': _('Title'),
            'content': _('Content'),
            'category': _('Category'),
            'language': _('Language'),
            'price': _('Price'),
        }
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': _('Enter a title for your template')}),
            'content': forms.TextInput(attrs={'placeholder': _('Enter a content for your template with variables in curly braces')}),
            'price': forms.NumberInput(attrs={'placeholder': _('Enter a price for your template')}),
        }

# Define a form for creating a prompt
class PromptCreateForm(forms.ModelForm):
    # Meta class for form options
    class Meta:
        # Specify the model and fields for the form
        model = Prompt
        fields = ['title', 'content', 'template', 'language', 'price']

        # Specify the labels and placeholders for the fields
        labels = {
            'title': _('Title'),
            'content': _('Content'),
            'template': _('Template'),
            'language': _('Language'),
            'price': _('Price'),
        }
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': _('Enter a title for your prompt')}),
            'content': forms.TextInput(attrs={'placeholder': _('Enter a content for your prompt without variables')}),
            'price': forms.NumberInput(attrs={'placeholder': _('Enter a price for your prompt')}),
        }
