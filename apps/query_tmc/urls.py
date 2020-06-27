from django.urls import path, include
from .views import Index
app_name="query_tmc" # spacename for app query_tmc

urlpatterns = [
    path('', Index.as_view(), name="index"),
]
