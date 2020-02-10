from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects/', include('projects.urls')),
    path('', include('homepage.urls')),
    path('weather/', include('weatherapp.urls'))
    #path('20f/', views.Home.as_view()),
]

urlpatterns += staticfiles_urlpatterns()
