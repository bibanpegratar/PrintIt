# todo/todo_api/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Printer, Task, CustomUser
from .serializers import PrinterSerializer, TaskSerializer
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token

@api_view(['GET'])
def show_all_user_printers(request):
    permission_classes = [permissions.IsAuthenticated]
    if request.method == 'GET':
        printers = Printer.objects.filter(user = request.user.id)
        serializer = PrinterSerializer(printers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_printer(request, id):
    permission_classes = [permissions.IsAuthenticated]
    if request.method == 'GET':
        printer = Printer.objects.get(id = id)
        serializer = PrinterSerializer(printer)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def show_all_printers(request):
    permission_classes = [permissions.IsAuthenticated]
    if request.method == 'GET':
        printers = Printer.objects.filter()
        serializer = PrinterSerializer(printers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_printer(request):
    permission_classes = [permissions.IsAuthenticated]
    if request.method == 'POST':
        user_id = Token.objects.get(key=request.auth.key).user_id
        data = {
            'type': request.data.get('type'), 
            'fillament_color': request.data.get('fillament_color'), 
            'material': request.data.get('material'),
            'speed': request.data.get('speed'),
            'price': request.data.get('price'),
            'latitude': request.data.get('latitude'),
            'longitude': request.data.get('longitude'),
            'user': user_id
        }
        serializer = PrinterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_task(request):
    permission_classes = [permissions.IsAuthenticated]
    if request.method == 'POST':
        user_id = Token.objects.get(key=request.auth.key).user_id
        data = {
            'file': request.data.get('file'),
            'fillament_color': request.data.get('fillament_color'), 
            'material': request.data.get('material'),
            'printer': request.data.get('printer'),
            'price' : request.data.get('price'),
            'user': user_id
        }
    serializer = TaskSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])      
def show_all_user_tasks(request):
    permission_classes = [permissions.IsAuthenticated]
    if request.method == 'GET':
        tasks = Task.objects.filter(user = request.user.id)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)