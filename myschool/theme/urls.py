from django.urls import include, path
from .views import home

urlpatterns = [
    path('', home, name='home'),
    path('highschool/', include('highschool.urls')),
]

