from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class SignupForm(UserCreationForm):
    email = forms.EmailField(
        label="",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Адрес электронной почты"}
        ),
    )
    first_name = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Имя"}),
    )
    last_name = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Фамилия"}
        ),
    )

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)

        self.fields["username"].widget.attrs["class"] = "form-control"
        self.fields["username"].widget.attrs["placeholder"] = "Имя пользователя"
        self.fields["username"].label = ""
        self.fields[
            "username"
        ].help_text = "<span class='form-text text-muted'> Имя пользователя </span>"

        self.fields["password1"].widget.attrs["class"] = "form-control"
        self.fields["password1"].widget.attrs["placeholder"] = "Пароль"
        self.fields["password1"].label = ""
        self.fields[
            "password1"
        ].help_text = (
            "<span class='form-text text-muted'> Пароль должен быть сложный </span>"
        )

        self.fields["password2"].widget.attrs["class"] = "form-control"
        self.fields["password2"].widget.attrs["placeholder"] = "Подтвердите пароль"
        self.fields["password2"].label = ""
        self.fields[
            "password2"
        ].help_text = (
            "<span class='form-text text-muted'> Пароли должны совпадать </span>"
        )
