from django.urls import path
from .import views

urlpatterns = [path('elements',views.Products,name='elements'),
               path('contact',views.Contact,name='contact'),
               path('destinations',views.Destination,name='destination'),
               path('index',views.Index,name='index'),
               path('news',views.News,name='news'),
               ]