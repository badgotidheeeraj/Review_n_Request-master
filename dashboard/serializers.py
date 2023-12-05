# serializers.py
from rest_framework import serializers
from .models import RequestModule, MasterModule, UserAccount


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ['id']

class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterModule
        fields = ['module_name']

class RequestSerializer(serializers.ModelSerializer):
    ModuleName = ModuleSerializer()
    username = UserSerializer()

    class Meta:
        model = RequestModule
        fields = '__all__'
