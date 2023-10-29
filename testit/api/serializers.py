from rest_framework import serializers
from .models import Printer, Task

class PrinterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Printer
        fields =  "__all__"
        
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields =  "__all__"