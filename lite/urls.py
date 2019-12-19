from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views   
from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'lite'
urlpatterns=[
    path(r'', views.signup, name = 'signup'),
    # url(r'^accounts/login/$', views.login, {"next_page": '/'}), 
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)