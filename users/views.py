from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login
from django.core.mail import send_mail
from django.contrib.auth.views import LoginView
from .forms import CustomUserCreationForm, CustomAuthenticationForm


class RegisterView(CreateView):
    """
    Вью для регистрации нового пользователя.
    После успешного сохранения пользователя происходит автоматический вход и отправляется приветственное письмо.
    """
    form_class = CustomUserCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        # Сохраняем пользователя
        user = form.save()
        # Осуществляем вход пользователя
        login(self.request, user)
        # Отправляем приветственное письмо
        send_mail(
            subject='Добро пожаловать в SkyS!',
            message=f'Здравствуйте, {user.email}! Спасибо за регистрацию на нашем сайте.',
            from_email='from@example.com',  # Замените на реальный email отправителя или настройте в settings.py
            recipient_list=[user.email],
            fail_silently=False,
        )
        return super().form_valid(form)


class CustomLoginView(LoginView):
    """
    Вью для входа пользователя с использованием кастомной формы, где логин — email.
    """
    authentication_form = CustomAuthenticationForm
    template_name = 'users/login.html'
