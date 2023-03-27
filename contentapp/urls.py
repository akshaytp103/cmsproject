from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import ContentListCreateView, ContentDetailView

urlpatterns = [
   
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('contents/', ContentListCreateView.as_view(), name='content_list_create'),
    path('contents/<int:pk>/', ContentDetailView.as_view(), name='content_detail'),
]
