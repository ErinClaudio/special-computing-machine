from django.urls import path
from .views import HomePageView, emailView, successView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('email/', emailView, name='email'),
    path('success/', successView, name='success'),
]
