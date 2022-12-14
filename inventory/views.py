from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core.mixins.views import ArchiveViewMixin
from core.services import ArchiveService
from inventory.models import Material
from inventory.serializers import MaterialSerializer
from inventory.services import MaterialDestroyService


class MaterialViewSet(ModelViewSet,
                      ArchiveViewMixin):
    queryset = Material.objects.filter()
    serializer_class = MaterialSerializer

    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            updated_instance = ArchiveService(instance,
                                              self.serializer_class).update(**request.data)
            return Response(MaterialSerializer(updated_instance).data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, *args, **kwargs):
        return self.update(request, partial=True, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        try:
            MaterialDestroyService(self.get_object()).destroy()
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_204_NO_CONTENT)
