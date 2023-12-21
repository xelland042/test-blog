from django.shortcuts import render, redirect, get_list_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from account.forms import SignUpForm
from django.views import View, generic

User = get_user_model()


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if not user:
            messages.error(request, 'User not found, please try again!!!')
            return render(request, 'registration/login.html')
        login(request, user)
        messages.info(request, 'Login successfully!!!')
        return redirect('post:home')
    return render(request, 'registration/login.html')


def logout_view(request):
    logout(request)
    messages.info(request, 'Logout successfully')
    return redirect('account:login')


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # subject = 'Test project'
            # message = f'Hi there {user}, thank you for registering!'
            # email_form = settings.EMAIL_HOST_USER
            # recipient_list = [user.email, ]
            # send_mail(subject, message, email_form, recipient_list)
            messages.success(request, 'Authentication was successful')
            return redirect('blog-list')
    form = SignUpForm()
    context = {
        'form': form,
    }
    return render(request, 'registration/registration.html', context=context)


def password_restart_view(request):
    if request.method == 'POST':
        pass


class UserListView(View):
    template_name = 'registration/users_list.html'

    def get(self, request):
        users = self.get_object()
        context = {
            'users': users
        }
        return render(request, self.template_name, context=context)

    def get_object(self):
        return get_list_or_404(User)


class UserUpdateView(generic.UpdateView):
    template_name = 'registration/user_change.html'
    model = User
    fields = ('username', 'first_name', 'last_name', 'email', 'phone_number', 'bio', 'image')
