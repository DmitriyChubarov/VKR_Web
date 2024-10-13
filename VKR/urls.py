from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(),name='home'),
    path('bi_line', views.Bi_line.as_view(),name='bi_line')
]