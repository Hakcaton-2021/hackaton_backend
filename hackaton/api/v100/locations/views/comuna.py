from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import (
    AllowAny,
    DjangoModelPermissions,
    IsAdminUser,
    IsAuthenticated,
)
from rest_framework.response import Response

from hackaton.api.v100.locations.serializers.comuna import (
    CreateSerializer,
    ListSerializer,
    UpdateSerializer,
)
from hackaton.apps.locations.services import comuna as comuna_services
from hackaton.utils.lib.constants import DATA_NOT_FOUND, PERMISSIONS_ERROR, SERVER_ERROR


class ComunaViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    # GET: api/v100/locations/comuna/
    def list(self, request):
        comunas = comuna_services.get_all_comunas()
        serializer = ListSerializer(comunas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # POST: api/v100/locations/comuna/
    def create(self, request):
        if not request.user.is_staff:
            return Response(PERMISSIONS_ERROR, status=status.HTTP_403_FORBIDDEN)
        serializer = CreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                data={"message": "Comuna creada con exito"},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # GET: api/v100/locations/comuna/<pk>/
    def retrieve(self, request, pk):
        if not pk:
            return Response(DATA_NOT_FOUND, status=status.HTTP_404_NOT_FOUND)
        if not request.user:
            return Response(PERMISSIONS_ERROR, status=status.HTTP_403_FORBIDDEN)
        comuna = comuna_services.get_comuna_by_pk(pk=pk)
        if not comuna:
            return Response(DATA_NOT_FOUND, status=status.HTTP_404_NOT_FOUND)
        serializer = ListSerializer(comuna)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # PUT: api/v100/locations/comuna/<pk>/
    def update(self, request, pk):
        if not request.user.is_staff:
            return Response(PERMISSIONS_ERROR, status=status.HTTP_403_FORBIDDEN)
        if not pk:
            return Response(DATA_NOT_FOUND, status=status.HTTP_404_NOT_FOUND)
        comuna = comuna_services.get_comuna_by_pk(pk=pk)
        if not comuna:
            return Response(DATA_NOT_FOUND, status=status.HTTP_404_NOT_FOUND)
        serializer = UpdateSerializer(comuna, data=request.data)
        if serializer.is_valid():
            serializer.save(
                update_fields=[
                    "code",
                    "name",
                    "country",
                    "updated_at",
                ]
            )
            return Response(
                data={"message": "Comuna actualizada con exito"},
                status=status.HTTP_200_OK,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # PUT: api/v100/locations/comuna/<pk>/activate/
    @action(detail=True, methods=["put"], url_name="activate", url_path="activate")
    def activate(self, request, pk):
        if not request.user.is_staff:
            return Response(PERMISSIONS_ERROR, status=status.HTTP_403_FORBIDDEN)
        if not pk:
            return Response(DATA_NOT_FOUND, status=status.HTTP_404_NOT_FOUND)
        updated = comuna_services.activate_comuna_by_pk(pk=pk)
        if updated:
            return Response(
                data={"message": "Comuna activada con exito"}, status=status.HTTP_200_OK
            )
        return Response(SERVER_ERROR, status=status.HTTP_400_BAD_REQUEST)

    # PUT: api/v100/locations/comuna/<pk>/deactivate/
    @action(detail=True, methods=["put"], url_name="deactivate", url_path="deactivate")
    def deactivate(self, request, pk):
        if not request.user.is_staff:
            return Response(PERMISSIONS_ERROR, status=status.HTTP_403_FORBIDDEN)
        if not pk:
            return Response(DATA_NOT_FOUND, status=status.HTTP_404_NOT_FOUND)
        updated = comuna_services.deactivate_comuna_by_pk(pk=pk)
        if updated:
            return Response(
                data={"message": "Comuna desactivada con exito"},
                status=status.HTTP_200_OK,
            )
        return Response(SERVER_ERROR, status=status.HTTP_400_BAD_REQUEST)

    # GET: api/v100/locations/comuna/select_list/
    @action(
        detail=False, methods=["get"], url_name="select_list", url_path="select_list"
    )
    def select_list(self, request):
        comunas = comuna_services.get_active_comunas()
        if not comunas:
            return Response(DATA_NOT_FOUND, status=status.HTTP_404_NOT_FOUND)
        serializer = ListSerializer(comunas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
