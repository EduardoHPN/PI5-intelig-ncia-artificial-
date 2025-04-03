from django.urls import path

from recipes.views import home, Penal, EmBreve


urlpatterns = [
    path('', home),
    path('recipes/3/', Penal),
    path('recipes/2/', EmBreve),
    path('recipes/1/', EmBreve)

]
