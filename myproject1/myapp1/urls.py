from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.generic import RedirectView
from django.contrib import admin

from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('', views.login, name='login'),
    path('login', views.login, name='login'),
    path('userlogin', views.userlogin, name='userlogin'),
    path('reg', views.reg, name='reg'),
    path('logout', views.logout, name='logout'),
    path('viewlist', views.viewlist, name='viewlist'),
    path('profileupdate/<int:dataid>', views.profileupdate, name='profileupdate'),
    path('edituser/<int:dataid>', views.edituser, name='edituser'),
    path('deleteuser/<int:dataid>', views.deleteuser, name='deleteuser'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.MEDIA_URL)
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)