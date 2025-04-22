from django.urls import path
from recipes.views import *


urlpatterns = [
    path('home/', home, name ='home'),
    path('', Login),
    path('cadastro/', Cadastro),
    path('recipes/3/', Penal),
    path('recipes/2/', EmBreve),
    path('recipes/1/', EmBreve),
    path('autenticar/', autenticar_usuario),
    path('recipes/arg-juridica/', ArgJuridica, name='argju'),
    path('recipes/defesa-preliminar/', defesa_preliminar ,name='preliminar') # nova rota
]
