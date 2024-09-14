from django.urls import path
from . import views

urlpatterns = [
    path('' , views.hello, name='hello'),
    path('e' , views.e, name='e'),
    path('page' , views.page, name='page'),

]