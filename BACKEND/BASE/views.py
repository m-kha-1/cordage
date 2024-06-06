
from BACKEND.settings import env as e
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.http import JsonResponse


from django.http import HttpResponse


from django.shortcuts import get_object_or_404


from django.db.models import F

# from .models import PRODUCTION,Task,Task2,Producer,CgArtist,Supervisor2,UserProfile
from .models import*
# from .serializers import ProdSerializer,TaskSerializer2,ProducerSerializer,CgArtist2Serializer,Supervisor2Serializer,TaskSerializer2_noId
from .serializers import *

import os

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated




  
# @api_view(['POST'])
# def newTask(request):
#     serializer=TaskSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()

    # return Response (serializer.data)
    
    
    
    
    
    
    
    


from BACKEND.settings import env as e
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

# from .models import Task2, Producer, CgArtist2, Supervisor2, PRODUCTION  # Assurez-vous d'importer PRODUCTION
from .models import *

from .serializers import TaskSerializer2, ProducerSerializer, CgArtist2Serializer, Supervisor2Serializer, TaskSerializer2_noId

import os



@api_view(['POST'])
def addProd(request):
    serializer=ProdSerializer(data=request.data)
    # main_folder = "PRODUCTION"


    
    if serializer.is_valid():
        serializer.save()
        
    # main_folder = serializer._validated_data.get("name") 
    # # pathApp =e.str("PROJECT_LOC")
    # pathApp='C:\apppp'
    # pathProduction=os.path.join(main_folder,pathApp,pathApp)
    
    # subfolders = ["lighting", "animation", "modelling","fx","compositing","surfacing","rigging"]
    # for subfolder in subfolders:
    #     os.makedirs(os.path.join(pathProduction, subfolder), exist_ok=True)    

    
    # main_folder =r"C:\ap" 
    main_folder =e.str("PROJECT_LOC")
    print(main_folder)
   
    

    # pathApp="nomdelaprod"
    pathProduction=serializer.validated_data.get("name")
    print(pathProduction)
    pathProduction=os.path.join(main_folder,pathProduction)
    print(pathProduction)
    subfolders = ["lighting", "animation", "modelling","fx","compositing","surfacing","rigging"]
    for subfolder in subfolders:
        os.makedirs(os.path.join(pathProduction, subfolder), exist_ok=True)  
        print("dossiers crees") 
    
    
    return Response (serializer.data)


@api_view(['POST'])
def newTask2(request):
    
    
    main_folder =e.str("PROJECT_LOC")
    #TaskSerializer2 pour la creation de la tache
    serializer=TaskSerializer2(data=request.data)
    
    #TaskSerializer2_noId pour obtenir nom du cgartist et nom production relative et non leur id 
    serializerNoId=TaskSerializer2_noId(data=request.data)
    
 
   
    if serializerNoId.is_valid():
        serializerNoId.save()

        
        print("data serialisées",serializerNoId.data)
        

        nameProduction=serializerNoId.data["production_name"]
        print(nameProduction)
        nameCgArtist=serializerNoId.data["cgArtist_name"]
        
        nametaskType=serializerNoId.data["type"]
        
        nametask=serializerNoId.data["name"]
        
        print("main_folder:", main_folder)
        print("nameProduction:", nameProduction)
        print("nameTaskType:", nametaskType)
        print("nameCgArtist:", nameCgArtist)
        
        # pathTask_work=os.path.join(main_folder,nameProduction,nametaskType,nameCgArtist,"WORK")
        # pathTask_publish=os.path.join(main_folder,nameProduction,nametaskType,nameCgArtist,"PUBLISH") 
        
        pathTask_work=os.path.join(main_folder,nameProduction,nametaskType,nametask,"WORK",nameCgArtist)
        pathTask_publish=os.path.join(main_folder,nameProduction,nametaskType,nametask,"PUBLISH") 
       
        if not os.path.exists(pathTask_work):
            os.makedirs(pathTask_work)
        if not os.path.exists(pathTask_publish):
            os.makedirs(pathTask_publish)


    return Response (serializerNoId.data)



# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# import os

# class NewTask2View(APIView):
#     """
#     Créer une nouvelle tâche et les dossiers associés.
#     """
#     def post(self, request, format=None):
#         serializer = TaskSerializer2(data=request.data)
#         serializerNoId = TaskSerializer2_noId(data=request.data)
        
#         if serializerNoId.is_valid():
#             print("data serialisées", serializerNoId.validated_data)
            
#             nameProduction = serializerNoId.validated_data.get("production_name")
#             print(nameProduction)
#             nameCgArtist = serializerNoId.validated_data.get("cgArtist_name")
#             nametaskType = serializerNoId.validated_data.get("type")
            
#             main_folder = os.environ.get("PROJECT_LOC")
#             pathTask_work = os.path.join(main_folder, nameProduction, nametaskType, nameCgArtist, "WORK")
#             pathTask_publish = os.path.join(main_folder, nameProduction, nametaskType, nameCgArtist, "PUBLISH")
            
#             if not os.path.exists(pathTask_work):
#                 os.makedirs(pathTask_work)
#             if not os.path.exists(pathTask_publish):
#                 os.makedirs(pathTask_publish)

#             serializerNoId.save()
#             return Response(serializerNoId.data, status=status.HTTP_201_CREATED)
#         return Response(serializerNoId.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def prod(request):
    productions=PRODUCTION.objects.all()
    serializer=ProdSerializer(productions,many=True)
    
    return Response (serializer.data)


# @api_view(['GET'])
# def gettasks(request):
#     tasks=Task.objects.all()
#     serializer=TaskSerializer(tasks,many=True)
    
#     return Response (serializer.data)

# @api_view(['GET'])
# def gettasks2(request):
#     tasks2=Task2.objects.all()
#     serializer=TaskSerializer(tasks2,many=True)
    
#     return Response (serializer.data)

@api_view(['GET'])
def gettasks2(request):
    tasks2=Task2.objects.all()
    serializer=TaskSerializer2_noId(tasks2,many=True)
    
    return Response (serializer.data)


@api_view(['GET'])
def gettask2Id(request,task_id):
    task2=Task2.objects.get(id=task_id)
    serializer=TaskSerializer2_noId(task2,many=False)
    
    return Response (serializer.data)



@api_view(['GET'])
def prodId(request,prod_id):
   production =PRODUCTION.objects.get(id=prod_id)
   serializer=ProdSerializer(production,many=False)
   
   return Response (serializer.data)

@api_view(['GET'])
def get_producer(request):
    producer=Producer2.objects.all()
    serializer=Producer2Serializer(producer,many=True)
    
    return Response (serializer.data)
        
@api_view(['GET'])
def get_artists(request):
    artists=CgArtist3.objects.all()
    serializer=CgArtist2Serializer(artists,many=True)
    
    return Response (serializer.data)


@api_view(['GET'])
def get_supervisors(request):
    supervisors=Supervisor2.objects.all()
    serializer=Supervisor2Serializer(supervisors,many=True)
    
    return Response (serializer.data)
        

@api_view(['PUT'])
def updateId(request,prod_id):
   production =PRODUCTION.objects.get(id=prod_id)
   serializer=ProdSerializer(production,data=request.data)
   if serializer.is_valid():
       serializer.save()
       return Response (serializer.data)
   
   return Response(serializer.errors, status=400)



@api_view(['PUT'])
def updateTask2(request,task2_id):
   task2 =Task2.objects.get(id=task2_id)
   serializer=TaskSerializer2_noId(task2,data=request.data)
   if serializer.is_valid():
       serializer.save()
       return Response (serializer.data)
   
   return Response(serializer.errors, status=400)



@api_view(['PUT'])
def updatetask2Version(request, id):
    try:
        mon_objet = Task2.objects.get(id=id)
        mon_objet.versions = F('versions') + 1
        mon_objet.save()
        return Response({"message": "La valeur de 'versions' a été incrémentée."})
    except Task2.DoesNotExist:
        return Response({"error": "L'objet n'existe pas."}, status=404)








@api_view(['DELETE'])
def delId(request,prod_id):
    
   production =PRODUCTION.objects.get(id=prod_id)
   
   production.delete() 
   return HttpResponse ("production deleted successfully")



@api_view(['DELETE'])
def delTaskId(request,prod_id):
    
   task2 =Task2.objects.get(id=prod_id)
   
   task2.delete() 
   return HttpResponse ("production deleted successfully")



@api_view(['GET'])
def get_PRODUCTION_id(request, task_id):
    task = get_object_or_404(Task2, pk=task_id)
    production_id = task.PRODUCTIONId.id if task.PRODUCTIONId else None
    return Response({'production_id': production_id})

# @api_view(['GET'])
# def get_task_ids_by_production(request, production_id):
#     production = get_object_or_404(PRODUCTION, pk=production_id)
#     # task_ids = production.PRODUCTIONTasks.values_list('id', flat=True)
#     # return Response({'task_ids': list(task_ids)})
#     tasks = production.PRODUCTIONTasks.all()
#     serializer = TaskSerializer(tasks, many=True)
#     return Response({'tasks': serializer.data})



###############CORRECTION IN ###
# def get_task2_ids_by_production(request, production_id):
#     get_task2_ids_by_production(request, production_id):
        
        
#     production = get_object_or_404(PRODUCTION, pk=production_id)
#     production = get_object_or_404(PRODUCTION, pk=production_id)
    
    
#     tasks2 = Task2.objects.filter(PRODUCTIONId=production_id)
#     production_tasks = production.production_tasks2.all()
    
#     serializer = TaskSerializer2(tasks2, many=True)
#     serializer = TaskSerializer(production_tasks, many=True)
    
    
    
#     return Response(serializer.data) # Retourne directement les données sérialisées
#     return Response(serializer.data)

###############CORRECTION OUT###






@api_view(['GET'])
def get_task2_ids_by_production(request, production_id):
    # Récupérer l'objet Production
    production = get_object_or_404(PRODUCTION, pk=production_id)
    
    # Récupérer toutes les tâches associées à cette production
    tasks2 = production.production_tasks2.all()  # production_tasks2 est le related_name défini dans la classe Task2
    
    # Serializer les tâches
    serializer = TaskSerializer2_noId(tasks2, many=True)
    
    # Retourner la réponse JSON
    return Response(serializer.data)






##########AUTH


def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirection vers la page d'accueil après la connexion
        else:
            # Gérer le cas où les informations d'identification sont incorrectes
            # Par exemple, afficher un message d'erreur
            pass
    return render(request, 'login.html')


def home_view(request):
    return render(request, 'home.html')


def custom_logout(request):
    logout(request)
    return render(request, 'logout.html')

@api_view(['POST'])
def createUser(request):
           type=request.data.get("type")
           role=request.data.get("role")
           name=request.data.get("name")
           email=request.data.get("email")
           password=request.data.get("password")
           
           
           if type == "producer":
               user = User.objects.create_user(username=name, email=email, password=password)
               profile = UserProfile.objects.create(user=user, type=type)
               producer = Producer2.objects.create(user=user,name=name)
            
           if type == "supervisor":
               user = User.objects.create_user(username=name, email=email, password=password)
               profile = UserProfile.objects.create(user=user, type=type)
               supervisor = Supervisor2.objects.create(user=user,name=name)
               
            
           if type == "cgartist":
               user = User.objects.create_user(username=name, email=email,password=password)
               profile = UserProfile.objects.create(user=user, type=type)
               cgartist = CgArtist3.objects.create(user=user,name=name,role=role)
               
           
           
           return JsonResponse({'message': 'User created successfully'}, status=201)
       
       
#####authorization########

from rest_framework_simplejwt.views import TokenObtainPairView

class TokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        return response










