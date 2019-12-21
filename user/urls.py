from django.urls import path, include
from django.contrib.auth import views as auth_views


urlpatterns = [
    # path('login/', auth_views.login,  name='login')
    path('', include('django.contrib.auth.urls'))
]
