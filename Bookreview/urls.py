from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='reviews'),
    url(r'^gallery/', views.gallery, name='reviews'),

]