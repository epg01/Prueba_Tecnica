"""extract_pdfs URL Configuration
"""
from django.contrib import admin
from django.urls import path
from extract_pdfs import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('extract/', views.extract),
    path('db_data/', views.db_data),
]
