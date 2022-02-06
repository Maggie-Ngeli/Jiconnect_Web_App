from rest_framework import serializers
from .models import Customer, Application, Employee, Appliances

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'


class AppliancesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appliances
        fields = '__all__'
