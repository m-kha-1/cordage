from django.shortcuts import render
from bs4 import BeautifulSoup
from urllib.parse import urljoin

from rest_framework.response import Response
from rest_framework.decorators import api_view
from requests.exceptions import RequestException

import requests
import subprocess


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
    
# @api_view(['GET'])
# def liste_fichiers(request, np):
#      try:
#         url = f'http://localhost:8080/{np}/'
#         path_img=  '.png'
#      except RequestException as e:
#          return Response ({'message': 'Erreur de connexion au serveur'},status=500)
        


@api_view(['GET'])
def image_production(request, np):
    try:
        # Construire l'URL de base
        url_base = f'http://localhost:8080/{np}/'

        # Faire une requête GET pour obtenir le contenu de la page
        response = requests.get(url_base)
        response.raise_for_status()

        # Analyser le contenu HTML de la page
        soup = BeautifulSoup(response.text, "html.parser")
        # print(soup)

        # Trouver tous les liens dans la page
        links = soup.find_all("a")

        # Initialiser une liste pour stocker les chemins des images
        image_paths = []

        # Parcourir tous les liens trouvés
        for link in links:
            href = link.get("href")
            # Vérifier si le lien pointe vers une image.jpg
            if href and href.endswith('.jpg'):
                # Construire le chemin complet de l'image
                full_path = urljoin(url_base, href)
                # Ajouter le chemin de l'image à la liste
                image_paths.append(full_path)

        # Renvoyer les chemins des images en utilisant Response
        return Response(image_paths, status=200)

    except requests.RequestException as e:
        # Gérer les exceptions de requête
        return Response({'message': 'Erreur de connexion au serveur distant'}, status=500)
    
    
    
    
    
    
    
    
    
@api_view(['GET'])
def liste_scenes(request, np, tt,nt):
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
        PATHS = [path for path in PATHS if path.endswith('.blend')]
        
        return Response(PATHS)

    except RequestException as e:
        return Response({'message': 'Erreur de connexion au serveur distant'}, status=500)
    
    
    
    
    import os
from django.http import JsonResponse
from rest_framework.decorators import api_view


## sans http server
@api_view(['GET'])
def liste_scenes2(request, np, tt, nt):
    # Chemin de base du répertoire où sont stockées les scènes Blender
    base_dir = os.path.join('C:\\CORD', np, tt, nt, 'PUBLISH')

    try:
        # Vérifier si le répertoire existe
        if not os.path.exists(base_dir):
            return JsonResponse({'message': 'Directory does not exist'}, status=404)

        # Lister tous les fichiers .blend dans le répertoire
        all_files = [os.path.join(root, file)
                     for root, dirs, files in os.walk(base_dir)
                     for file in files
                     if file.endswith('.blend')]

        return JsonResponse(all_files, safe=False)

    except Exception as e:
        return JsonResponse({'message': str(e)}, status=500)
    
    
    
    
   



@api_view(['POST'])
def lancer_scene(request):
    # Extraire le chemin du fichier .blend des données POST
    blend_file_path = request.data.get('blend_file_path')

    # Vérifier si le chemin du fichier est fourni et valide
    if not blend_file_path or not os.path.exists(blend_file_path):
        return JsonResponse({'message': 'Invalid or non-existent file path'}, status=400)

    # Chemin vers l'exécutable Blender
    blender_path = r"C:\Program Files\Blender Foundation\Blender 4.2\blender.exe"
    
    try:
        # Lancer Blender avec le fichier .blend
        subprocess.Popen([blender_path, blend_file_path])
        return JsonResponse({'message': 'Scene launched successfully'}, status=200)
    except Exception as e:
        return JsonResponse({'message': str(e)}, status=500)
