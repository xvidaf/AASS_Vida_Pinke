from EntityProvider.models import Predmet
from rest_framework import serializers, viewsets

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
    detaily = serializers.CharField(max_length=100)
    nazov = serializers.CharField(max_length=100)
    trieda = ClassSerializer()

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Predmet.objects.create(**validated_data)


# ViewSets define the view behavior.
class HourViewSet(viewsets.ModelViewSet):
    queryset = Predmet.objects.all()
    serializer_class = HourSerializer