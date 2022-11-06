from django.urls import path
from api import views

urlpatterns = [
    path('get/<int:year>/<int:month>/<slug:slug>/', views.SensorMixinView.as_view())
]
