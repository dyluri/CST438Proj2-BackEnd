from rest_framework import serializers
from base.models import Lists
from base.models import User

class ListsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lists

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'