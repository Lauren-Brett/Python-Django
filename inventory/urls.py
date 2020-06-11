from django.urls import path
from . import views

urlpatterns = [
    #-- path for us:
    # -- views telling us which page to view, link to then the name index
    path("", views.index, name='index'),
]