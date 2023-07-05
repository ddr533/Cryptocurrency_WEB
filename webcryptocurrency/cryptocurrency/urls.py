from django.urls import path
from .views import get_cryptocurrency


app_name = 'cryptocurrency'

urlpatterns = [
    path('', get_cryptocurrency, name='main')
]
