from django.urls import path
from .views import liste_fichiers,image_production,liste_scenes,liste_scenes2,lancer_scene,hello_view

urlpatterns = [
    path('test',hello_view),
    path('liste-fichiers/<str:np>/<str:tt>/<str:nt>/', liste_fichiers, name='liste_fichiers'),
    path('liste-scenes/<str:np>/<str:tt>/<str:nt>/', liste_scenes, name='liste_fichiers'),
    path('liste-scenes2/<str:np>/<str:tt>/<str:nt>/', liste_scenes2, name='liste_fichiers'),
    path('image_production/<str:np>/', image_production, name='image_production'),
     path('api/lancer_scene/', lancer_scene, name='lancer_scene'),
   
    
]
