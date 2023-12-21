from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

from account.views import login_view, sign_up, logout_view
from account.views import UserListView, UserUpdateView

app_name = 'account'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('registration/', sign_up, name='registration'),
    path('users/', UserListView.as_view(), name='users'),
    path('change-password/', auth_views.PasswordChangeView.as_view(template_name='registration/change_password.html',
                                                            success_url=reverse_lazy('home')),
         name='change-password'),
    path('update-user/<int:pk>', UserUpdateView.as_view(success_url=reverse_lazy('home')), name='user-update'),
]
