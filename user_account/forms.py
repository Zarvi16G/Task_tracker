from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import UserAccount

class UserAccountCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Correo Electrónico')
    # Añade campos del perfil si quieres que se registren desde el principio
    birth_date = forms.DateField(required=False, label='Fecha de Nacimiento', widget=forms.DateInput(attrs={'type': 'date'}))
    phone_number = forms.CharField(max_length=15, required=False, label='Número de Teléfono')


    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email',) # 'email' es del modelo User por defecto

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este correo electrónico ya está registrado.")
        return email

    # Sobreescribimos el método save para guardar el User y el UserAccount
    def save(self, commit=True):
        user = super().save(commit=commit) # Esto guarda el User y dispara la señal post_save
        # user.email = self.cleaned_data['email'] # El email ya debería estar en el User por defecto si lo pasas en fields
        return user # Asegúrate de que devuelve el objeto User

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Username'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label='Password'
    )

    class Meta:
        model = UserAccount
        fields = ('username', 'password')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'username': 'Username',
            'password': 'Password',
        }
        help_texts = {
            'username': 'Enter your username.',
            'password': 'Enter your password.',
        }
        error_messages = {
            'username': {
                'required': 'Username is required.',
            },
            'password': {
                'required': 'Password is required.',
            },
        }
