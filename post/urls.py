from django.urls import path

# from post.views import home
from post.views import PostListView, PostDetailView

app_name = 'post'

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('<int:pk>/', PostDetailView.as_view(), name='detail'),
]