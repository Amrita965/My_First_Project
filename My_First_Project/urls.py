
from django.contrib import admin
from django.urls import path
from first_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('musicians/', views.displayMusicians, name="muscians"),
    path('form/', views.form, name="form"),
    path('musician-form/', views.django_form, name="musicanform")
]
