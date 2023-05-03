from django.urls import path, include
from EntityProvider.models import Predmet
from rest_framework import routers, serializers, viewsets

class TeacherSerializer(serializers.Serializer):
    bydlisko = serializers.CharField(max_length=255)
    meno = serializers.CharField(max_length=255)
    priezvisko = serializers.CharField(max_length=255)
    rodneCislo = serializers.CharField(max_length=255)
    jeMuz = serializers.BooleanField()

class ClassSerializer(serializers.Serializer):
    rocnik = serializers.CharField(max_length=5)
    nazov = serializers.CharField(max_length=100)
    ucitel = TeacherSerializer()

class HourSerializer(serializers.Serializer):
    id = serializers.PrimaryKeyRelatedField(queryset=Predmet.objects.all())
    detaily = serializers.CharField(max_length=100)
    nazov = serializers.CharField(max_length=100)
    trieda = ClassSerializer()


# ViewSets define the view behavior.
class HourViewSet(viewsets.ModelViewSet):
    queryset = Predmet.objects.all()
    serializer_class = HourSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'hours', HourViewSet)

urlpatterns = [
    path('', include(router.urls))
]
