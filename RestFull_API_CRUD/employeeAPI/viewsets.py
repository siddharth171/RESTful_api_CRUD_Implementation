from rest_framework import viewsets
from . import models
from . import serializers


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializers

""" internally the serializers will create classes like 
    list(), retrieve(), create(), update() and destroy() """