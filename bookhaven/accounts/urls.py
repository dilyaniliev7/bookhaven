from django.urls import path

from bookhaven.accounts.views import SignUpView, SignInView

urlpatterns = (
    path('register/', SignUpView.as_view(), name='register'),
    path('login/', SignInView.as_view(), name='login'),
)
