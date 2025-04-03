from django.urls import path
 
from forms.views import register_view
 
urlpatterns = [
    path('register/', register_view),

]
