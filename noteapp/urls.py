from django.urls import path 
from .import views 
from django.shortcuts import redirect
from .views import notes, note_detail, search_notes
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path("notes/", views.notes, name="notes"),
    path("notes/<slug:slug>/", views.note_detail, name="note-detail"),
    # path("", lambda request: redirect('notes/')),  # Redirect root URL to /notes/
    path("notes-search/", views.search_notes, name='notes-search'),

    # Authentication routes
    path('register/', views.register_user, name='register'),  # User registration
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Obtain JWT token
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refresh JWT token
]