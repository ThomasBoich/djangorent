from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView, LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import LoginForm, CustomUserCreationForm, CustomUserChangeForm
from users.models import CustomUser


# Create your views here.
class AppLogoutView(LogoutView):
    def get_success_url(self):
        return redirect('login')


class AppLoginView(LoginView):
    form_class = LoginForm
    template_name = 'users/login.html'
    success_url = reverse_lazy('dash')

    def get_success_url(self):
        return reverse_lazy('dash')

    redirect_authenticated_user = True


class AppRegistration(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('dash')


def user_info(request, user_id):
    user = request.user
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'title_page': 'Настройки профиля',
        'form': form,
        'back_button': True,
    }
    return render(request, 'users/user.html', context)


def user_profile(request, user_id):
    context = {
        'title_page': 'Настройки профиля',
        'user': CustomUser.objects.get(id=user_id),
        'back_button': True,
    }
    return render(request, 'users/profile.html', context)


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = CustomUserChangeForm(instance=request.user)

    context = {'form': form, 'back_button': True,}
    return render(request, 'profile/edit_profile.html', context)