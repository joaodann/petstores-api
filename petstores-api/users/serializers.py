from rest_framework import serializers
from .models import PetStore

class PetStoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = PetStore
        fields = ('id', 'name', 'zip_code', 'neighborhood', 'latitude', 'longitude', 'species',)

        def create(self, validated_data):
            pet_store = PetStore.objects.create(**validated_data)
            return pet_store
