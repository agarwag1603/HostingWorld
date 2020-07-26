from django import forms

from .models import registrationForm,SignupForm


class formView(forms.ModelForm):
    Password = forms.CharField(widget=forms.PasswordInput)
    ConPassword = forms.CharField(widget=forms.PasswordInput)
    FirstName=forms.CharField(widget=forms.TextInput)
    LastName = forms.CharField(widget=forms.TextInput)
    UserName = forms.CharField(widget=forms.TextInput)
    Email = forms.CharField(widget=forms.TextInput)

    class Meta:
        model = registrationForm
        fields = ['FirstName', 'LastName', 'UserName', 'Email','Password','ConPassword']
    #
    # def clean_FirstName(self):
    #     FirstName = self.cleaned_data.get('FirstName')
    #     for i in registrationForm.objects.all():
    #         if i.FirstName == FirstName:
    #             raise forms.ValidationError("Name already Available")
    #         return FirstName


class formSign(forms.ModelForm):
    Password = forms.CharField(widget=forms.PasswordInput)
    UserName = forms.CharField(widget=forms.TextInput)
    Email = forms.CharField(widget=forms.TextInput)

    class Meta:
        model = SignupForm
        fields = ['UserName', 'Email','Password']