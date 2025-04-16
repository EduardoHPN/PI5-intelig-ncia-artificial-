from django.urls import path

from recipes.views import home, Penal, EmBreve, Login


urlpatterns = [
    path('home/', home),
    path('', Login),
    path('recipes/3/', Penal),
    path('recipes/2/', EmBreve),
    path('recipes/1/', EmBreve)
]
