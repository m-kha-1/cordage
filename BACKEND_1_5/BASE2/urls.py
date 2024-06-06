from django.urls import path
from .views import liste_fichiers,hello_view

urlpatterns = [
    path('test',hello_view),
    path('liste-fichiers/<str:np>/<str:tt>/<str:nt>/', liste_fichiers, name='liste_fichiers'),
    
]
