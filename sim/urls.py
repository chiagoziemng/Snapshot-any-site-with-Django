from django.urls import path
from sim.views import CaptureView, capture_page



urlpatterns = [
    path('capture/', capture_page, name='capture_page'),
    path('capture-image/', CaptureView.as_view(), name='capture_image'),
]