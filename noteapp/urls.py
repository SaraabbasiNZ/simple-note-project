from django.urls import path 
from .import views 
from django.shortcuts import redirect


urlpatterns = [
    path("notes/", views.notes, name="notes"),
    path("notes/<slug:slug>/", views.note_detail, name="note-detail"),
    path("", lambda request: redirect('notes/')),  # Redirect root URL to /notes/
    path("notes-search/", views.search_notes, name='notes-search')
]