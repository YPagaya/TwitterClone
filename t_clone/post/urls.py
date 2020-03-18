from django.urls import path

from . import views
#urlpatterns = [
#    path('', views.index, name='index'),
#]

urlpatterns = [
    path('', views.post_list, name='post_list'),
]