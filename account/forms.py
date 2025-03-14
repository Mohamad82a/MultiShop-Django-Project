from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from .models import User, Address
from django.core import validators

class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""

    password1 = forms.CharField(label="گذرواژه ", widget=forms.PasswordInput)
    password2 = forms.CharField(label="تایید گذرواژه ", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["phone",]

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ["phone", "password", "is_active", "is_admin"]

# def start_with_0(value):
#     if value[0] != 0:
#         raise ValidationError('Your phone number should start with 0.(Ex: 09xxxxxxxxx)')


class LoginForm(forms.Form):
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': "form-control"}))

    # def clean_phone(self):
    #     phone = self.cleaned_data.get('phone')
    #     if len(phone) > 11:
    #         raise ValidationError("Invalid value: Phone number %(value)s is invalid" , code='invalid', params={'value': f'{phone}'},)
    #
    #     return phone
    #

class RegisterForm(forms.Form):
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}),validators=[validators.MaxLengthValidator(11)])

class CheckOtpForm(forms.Form):
    code = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}),validators=[validators.MaxLengthValidator(5)])


# class RegistrationForm(forms.ModelForm):
#     password = forms.CharField(label='Password', widget=forms.PasswordInput)
#
#     class Meta:
#         model = User
#         fields = ('phone', 'full_name', 'melicode','email', 'password',)
#
#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data["password"])
#
#         if commit:
#             user.save()
#         return user


class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['phone', 'full_name', 'melicode','email', 'password1', 'password2']

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['full_name', 'phone','melicode','email',]

    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control rounded'})

class AddressCreationForm(forms.ModelForm):
    user = forms.IntegerField(required=False)
    class Meta:
        model = Address
        fields = '__all__'


