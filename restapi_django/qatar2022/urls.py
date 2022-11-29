from django.urls import path

from qatar2022 import views

urlpatterns = [
    path('', views.get_qatar_2022_game_list)
]
