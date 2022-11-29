from django.urls import path

from alivecheck import views

urlpatterns = [
    path('', views.index)
]
