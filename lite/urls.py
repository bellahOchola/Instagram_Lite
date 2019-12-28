from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views   
# from django.conf.urls import url
from django.urls import path
from . import views
from django.conf.urls import include

app_name = 'lite'
urlpatterns=[
    path('', views.signup, name='signup'),
    path('account/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)