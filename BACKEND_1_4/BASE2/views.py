from django.shortcuts import render
from bs4 import BeautifulSoup
from urllib.parse import urljoin

from rest_framework.response import Response
from rest_framework.decorators import api_view
from requests.exceptions import RequestException

import requests


from django.http import HttpResponse

def hello_view(request):
    return HttpResponse("Hello")


# def liste_fichiers(request):
   
#     url = 'http://localhost:8080/PROJECT_MOCK/'
#     response = requests.get(url)

#     if response.status_code == 200:
      
#         fichiers = response.json()
        
     
#         return Response(fichiers)
#     else:
#         # Retourner une réponse d'erreur si la requête a échoué
        # return Response({'message': 'Impossible de récupérer les fichiers'}, status=response.status_code)
# @api_view(['GET'])
# def liste_fichiers(request):
#     try:
        
#         url = "http://localhost:8080/PROJECT_MOCK/modelling/Pierre%20M/PUBLISH/"
#         response = requests.get(url)
        
#         response.raise_for_status()  # Vérifie si une erreur HTTP s'est produite
        
#         if response.content:  # Vérifie si la réponse contient du contenu
#             fichiers = response.json()
#             return Response(fichiers)
#         else:
#             return Response({'message': 'La réponse est vide'}, status=204)  # Réponse vide
#     except RequestException as e:
#         return Response({'message': 'Erreur de connexion au serveur distant'}, status=500)
    
    



import os
import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view
from requests.exceptions import RequestException

@api_view(['GET'])
def liste_fichiers(request, np, tt,nt):
    def versions_list_images(url, depth=0, max_depth=3):
        try:
            response = requests.get(url)
            response.raise_for_status()
            
            if response.status_code == 200:
                content = response.text
                soup = BeautifulSoup(content, "html.parser")
                paths = soup.find_all("a")
                PATHS = []

                for p in paths:
                    path = urljoin(url, p.get("href"))
                    PATHS.append(path)

                if depth < max_depth:
                    for path in PATHS[:]:  # Utilisation de [:] pour éviter les modifications en cours d'itération
                        sub_paths = versions_list_images(path, depth + 1, max_depth)
                        PATHS.extend(sub_paths)

                return PATHS

        except RequestException as e:
            return []

    try:
        url = f'http://localhost:8080/{np}/{tt}/{nt}/PUBLISH/'
        PATHS = versions_list_images(url)
        
        # Filtrer les chemins pour ne conserver que ceux se terminant par '.png'
        PATHS = [path for path in PATHS if path.endswith('.png')]
        
        return Response(PATHS)

    except RequestException as e:
        return Response({'message': 'Erreur de connexion au serveur distant'}, status=500)


    # return Response({'message': 'Une erreur s\'est produite'}, status=500)

