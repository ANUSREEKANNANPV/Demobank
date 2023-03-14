from django.urls import path
from.import views
urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('form', views.form, name='form'),
    path('BUTTON',views.BUTTON,name='BUTTON'),
]

