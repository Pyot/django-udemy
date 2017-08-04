from django import forms
from django.core import validators


# def check_for_letter(value):
#     if value[0].lower() != 'a':
#         raise forms.ValidationError('Name need to start with A Check file basicapp/forms.py')

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again.')
    text = forms.CharField(widget = forms.Textarea)
    # botcatcher = forms.CharField(required=False, widget=forms.HiddenInput,
    #                                 validators=[validators.MaxLengthValidator(0)])
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError("Make sure emails match!")

    #nazwa po celan_ musi byc pole ktore chcemy sprawdzic w tym wypadku botcatcher
    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError("Gotcha Bot!")
    #     return botcatcher
