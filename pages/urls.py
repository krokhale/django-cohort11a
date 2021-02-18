# pages/urls.py
from django.urls import path
# from .views import homePageView
from .views import HomePageView

urlpatterns = [
#     path('', homePageView, name='home')
    path('', HomePageView.as_view(), name='home'),

]
