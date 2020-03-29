from django.urls import include, path

from .views import LoginView, SignUpView

urlpatterns = [
    # auth:login - api/auth/login
    path(
        'login',
        LoginView.as_view(),
        name='login'
    ),
    path(
        'signup',
        SignUpView.as_view(),
        name='signup_student'
    ),
]