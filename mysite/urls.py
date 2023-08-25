from django.urls import path
from .import views
from mysite import views

urlpatterns = [
    path('',views.index,name="index"),
    # path('login/',views.login,name="login_page"),
    # path('sign_up/',views.sign_up,name="sign_up"),
    path('validation',views.validation,name="validation"),
    path('login',views.login,name="login"),
    path('wedding' ,views.wedding,name="wedding"),
    path('birthday',views.birthday,name="birthday"),
    path('contact',views.contact,name="contact"),
    path('booking',views.booking,name="booking"),
]
