from rest_framework import serializers
from .models import DbModel

class DbModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = DbModel
		fields: tuple = ('id','name','description','driver','host','port','username','password')
		
