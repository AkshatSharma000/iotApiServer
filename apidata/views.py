from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# from rest_framework import request

from .models import details
from .serializer import TaskSerializer

# Create your views here.
@api_view(['GET','POST'])
def home(request):
    
    if request.method == "GET":
        info = details.objects.all()
        serializer = TaskSerializer(info,many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT'])
def updating(request,slug):
    info = details.objects.get(userID=slug)
    if request.method == "GET":
        serializer = TaskSerializer(info,many=False)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = TaskSerializer(info, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)