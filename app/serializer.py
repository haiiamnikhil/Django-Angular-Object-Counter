from rest_framework import serializers
from .models import UploadData, Reports, UserModel, UserRecordCount


class DetectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadData
        fields = '__all__'


class CsvSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reports
        fields = ['report']
        

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'
        

class RecordsCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRecordCount
        fields = '__all__'