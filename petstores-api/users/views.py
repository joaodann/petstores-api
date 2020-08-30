from rest_framework import viewsets, mixins
from rest_framework import filters
from .models import PetStore
from .serializers import PetStoreSerializer


class PetStoreViewSet(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  viewsets.GenericViewSet):
    serializer_class = PetStoreSerializer
    queryset = PetStore.objects.all()
    search_fields = ['zip_code', 'neighborhood', 'species',]
    filter_backends = (filters.SearchFilter,)
