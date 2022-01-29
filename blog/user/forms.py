from django import forms


class ResgisterForm(forms.Form):
    username = forms.CharField(max_length=50, label='Istifadeci adi')
    password = forms.CharField(max_length=50, label='sifre', widget=forms.PasswordInput)
    confirm = forms.CharField(max_length=50, label='sifre tekrar', widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        confirm = self.cleaned_data.get('confirm')
        if password and confirm and password != confirm:
            raise forms.ValidationError("sehv bas verdi")
        values = {'username': username, 'password': password}
        return values

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'istifadeci adini yazin'}) , max_length=50, label='istifadeci adi')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'sifrenizi daxil edin'}), max_length=50, label='sifre')




