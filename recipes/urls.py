from django.urls import path
from recipes.views import *


urlpatterns = [
    path('home/', home, name ='home'),
    path('', Login),
    path('logout/', logout),
    path('cadastro/', Cadastro),
    path('recipes/3/', Penal), #form 1
    path('recipes/2/', EmBreve),
    path('recipes/1/', EmBreve),
    path('autenticar/', autenticar_usuario),
    path('recipes/generate-pdf/', relotorio, name='generate_pdf'),
    path('recipes/arg-juridica/', ArgJuridica, name='argju'),#form 3
    path('recipes/pedido/', pedido, name='pedido'),#form 4
    path('recipes/documentacao/', documentos, name='documentos'),#form 5
    path('recipes/defesa-preliminar/', defesa_preliminar ,name='preliminar') # nova rota #form 2
]
