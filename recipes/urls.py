from django.urls import path

from recipes.views import home, Penal


urlpatterns = [
    path('', home),
    path('recipes/3/', Penal)
]
