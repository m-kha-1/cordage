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




