from django.urls import path
from app import views
urlpatterns=[path("nanda",views.func,name="nanda")]