from django.urls import path
from .views import liste_fichiers,image_production,hello_view

urlpatterns = [
    path('test',hello_view),
    path('liste-fichiers/<str:np>/<str:tt>/<str:nt>/', liste_fichiers, name='liste_fichiers'),
    path('image_production/<str:np>/', image_production, name='image_production'),
    
]
