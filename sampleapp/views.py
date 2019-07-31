from rest_framework.viewsets import ModelViewSet
from .models import DbModel
from .serializers import DbModelSerializer

class DbModelViewset(ModelViewSet):
	queryset = DbModel.objects.all()
	serializer_class = DbModelSerializer
	lookup_field = "id"
	

