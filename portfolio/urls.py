from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from nearbyshops import views
from stockdata.views import values

urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects/', include('projects.urls')),
    path('', include('homepage.urls')),
    path('20f/', views.Home.as_view()),
    path('stockdata/', values(c, o))

]

urlpatterns += staticfiles_urlpatterns()
