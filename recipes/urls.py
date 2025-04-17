from django.urls import path

from recipes.views import home, Penal, EmBreve, Login, Cadastro, autenticar_usuario

urlpatterns = [
    path('home/', home),
    path('', Login),
    path('cadastro/', Cadastro),
    path('recipes/3/', Penal),
    path('recipes/2/', EmBreve),
    path('recipes/1/', EmBreve),
    path('autenticar/', autenticar_usuario),  # nova rota
]
