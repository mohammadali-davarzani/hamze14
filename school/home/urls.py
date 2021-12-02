from django.urls import path
from .views import HomePageView, AboutusPageView

urlpatterns = [ 
    path('', HomePageView.as_view(), name='home'),
    path('about_us/', AboutusPageView.as_view(), name='about_us')
]