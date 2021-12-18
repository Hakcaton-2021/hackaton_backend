from rest_framework import status, viewsets
from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import (
    AllowAny,
    DjangoModelPermissions,
    IsAdminUser,
    IsAuthenticated,
)
from rest_framework.response import Response

from hackaton.api.v100.business.serializers.cost_center import (
    CreateSerializer,
    ListSerializer,
    UpdateSerializer,
)
from hackaton.apps.business.services import cost_center as cost_center_services
from hackaton.utils.lib.constants import DATA_NOT_FOUND, SERVER_ERROR

class CostCenterViewset(viewsets.ViewSet):

    permission_classes = [AllowAny]
    # GET: api/v100/locations/costcenter/
    def list(self, request):
        cost_center = cost_center_services.get_all_cost_center()
        serializer = ListSerializer(cost_center, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # POST: api/v100/locations/costcenter/
    def create(self, request):
        serializer = CreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                data={"message": "Centro de Costo creado correctamente."}, status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # GET: api/v100/business/costcenter/<pk>/
    def retrieve(self, request, pk):
        if not pk:
            return Response(DATA_NOT_FOUND, status=status.HTTP_404_NOT_FOUND)
        cost_center = cost_center_services.get_cost_center_by_pk(pk=pk)
        if not cost_center:
            return Response(DATA_NOT_FOUND, status=status.HTTP_404_NOT_FOUND)
        serializer = ListSerializer(cost_center)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # PUT: api/v100/business/costcenter/<pk>/
    def update(self, request, pk):
        if not pk:
            return Response(DATA_NOT_FOUND, status=status.HTTP_404_NOT_FOUND)
        cost_center = cost_center_services.get_cost_center_by_pk(pk=pk)
        if not cost_center:
            return Response(DATA_NOT_FOUND, status=status.HTTP_404_NOT_FOUND)
        serializer = UpdateSerializer(cost_center, data=request.data)
        if serializer.is_valid():
            serializer.save(update_fields=[  
                "company",
                "name",
                "code",
                "parent",
                "updated_at",
            ])
            return Response(
                data={"message": "Centro de costos actualizado con exito"},
                status=status.HTTP_200_OK,
            )
        return Response(SERVER_ERROR, status=status.HTTP_400_BAD_REQUEST)

