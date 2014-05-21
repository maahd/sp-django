from django import forms
#from django.forms import
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from meddy1.models import DoctorSeeker

from django.core.mail import send_mail

from django.utils.translation import ugettext, ugettext_lazy as _


# class UserCreateForm(UserCreationForm):
#   name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'FirstName LastName'}))
#   email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Please enter a valid email address so we can reach you.'}))
    
#   username = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Your username (Only letters and numbers, no spaces allowed)'}))
#   password1 = forms.CharField(label="Password", max_length=200, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'For your security, we will never store your password as text.'}))
#   password2 = forms.CharField(label="Password Confirmation", max_length=200, widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Password Confirmation'}))
    
    
#   class Meta:
#       model = User
#       fields = ("name","username","password1","password2","email")
        
#   def save(self, commit=True,image=None):
#       user = super(UserCreateForm, self).save(commit=False)
#       user.email = self.cleaned_data["email"]
    
        
#       if commit:
#           user.save()
#           userProfile = DoctorSeeker(user=user, name=name, email=email)
            
#           userProfile.save()
#       return user

class UserCreationForm(forms.ModelForm):
    """
    A form that creates a user, with no privileges, from the given username and
    password.
    """
    error_messages = {
        'duplicate_username': _("A user with that username already exists."),
        'password_mismatch': _("The two password fields didn't match."),
    }
    name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'FirstName LastName'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Please enter a valid email address so we can reach you.'}))
    username = forms.RegexField(label=_("Username"), max_length=50,
        regex=r'^[\w.@+-]+$',
        help_text=_("Required. 30 characters or fewer. Letters, digits and "
                    "@/./+/-/_ only."),
        error_messages={
            'invalid': _("This value may contain only letters, numbers and "
                         "@/./+/-/_ characters.")})
    password1 = forms.CharField(label=_("Password"),
        widget=forms.PasswordInput)
    password2 = forms.CharField(label=_("Password confirmation"),
        widget=forms.PasswordInput,
        help_text=_("Enter the same password as above, for verification."))

    class Meta:
        model = User
        fields = ("username",)

    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]
        try:
            User._default_manager.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(
            self.error_messages['duplicate_username'],
            code='duplicate_username',
        )

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        fullName = self.cleaned_data["name"]
        Email = self.cleaned_data["email"]


        if commit:
            user.save()
            userProfile = DoctorSeeker(user=user, name=fullName, email=Email)
            userProfile.save()

        return user


