from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views   
from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'lite'
urlpatterns=[
    path(r'', views.signup, name = 'signup'),
    path(r'login/', views.login_user, name = 'login'), 
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)