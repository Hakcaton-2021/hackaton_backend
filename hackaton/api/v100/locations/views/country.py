from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import (
    AllowAny,
    DjangoModelPermissions,
    IsAdminUser,
    IsAuthenticated,
)
from rest_framework.response import Response

from hackaton.api.v100.locations.serializers.country import (
    CreateSerializer,
    ListSerializer,
    UpdateSerializer,
)
from hackaton.apps.locations.services import country as country_services
from hackaton.utils.lib.constants import (
    DATA_NOT_FOUND,
    PERMISSIONS_ERROR,
    SERVER_ERROR,
)


class CountryViewset(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    # GET: api/v100/locations/country/
    def list(self, request):
        country = country_services.get_all_countries()
        serializer = ListSerializer(country, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # POST: api/v100/locations/country/
    def create(self, request):
        if not request.user.is_staff:
            return Response(PERMISSIONS_ERROR, status=status.HTTP_403_FORBIDDEN)
        serializer = CreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                data={"message": "Pais creado con exito"}, status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # GET: api/v100/locations/country/<pk>/
    def retrieve(self, request, pk):
        if not pk:
            return Response(DATA_NOT_FOUND, status=status.HTTP_404_NOT_FOUND)
        country = country_services.get_country_by_pk(pk=pk)
        if not country:
            return Response(DATA_NOT_FOUND, status=status.HTTP_404_NOT_FOUND)
        serializer = ListSerializer(country)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # PUT: api/v100/locations/country/<pk>/
    def update(self, request, pk):
        if not request.user:
            return Response(PERMISSIONS_ERROR, status=status.HTTP_403_FORBIDDEN)
        if not pk:
            return Response(DATA_NOT_FOUND, status=status.HTTP_404_NOT_FOUND)
        country = country_services.get_country_by_pk(pk=pk)
        if not country:
            return Response(DATA_NOT_FOUND, status=status.HTTP_404_NOT_FOUND)
        serializer = UpdateSerializer(country, data=request.data)
        if serializer.is_valid():
            serializer.save(update_fields=["code","name", "updated_at"])
            return Response(
                data={"message": "Pais actualizado con exito"},
                status=status.HTTP_200_OK,
            )
        return Response(SERVER_ERROR, status=status.HTTP_400_BAD_REQUEST)

    # PUT: api/v100/locations/country/<pk>/activate/
    @action(detail=True, methods=["put"], url_name="activate", url_path="activate")
    def activate(self, request, pk):
        if not request.user.is_staff:
            return Response(PERMISSIONS_ERROR, status=status.HTTP_403_FORBIDDEN)
        if not pk:
            return Response(DATA_NOT_FOUND, status=status.HTTP_404_NOT_FOUND)
        updated = country_services.activate_country_by_pk(pk=pk)
        if updated:
            return Response(
                data={"message": "Pais activado con exito"}, status=status.HTTP_200_OK
            )
        return Response(SERVER_ERROR, status=status.HTTP_400_BAD_REQUEST)

    # PUT: api/v100/locations/country/<pk>/deactivate/
    @action(detail=True, methods=["put"], url_name="deactivate", url_path="deactivate")
    def deactivate(self, request, pk):
        if not request.user.is_staff:
            return Response(PERMISSIONS_ERROR, status=status.HTTP_403_FORBIDDEN)
        if not pk:
            return Response(DATA_NOT_FOUND, status=status.HTTP_404_NOT_FOUND)
        updated = country_services.deactivate_country_by_pk(pk=pk)
        if updated:
            return Response(
                data={"message": "Pais desactivado con exito"},
                status=status.HTTP_200_OK,
            )
        return Response(SERVER_ERROR, status=status.HTTP_400_BAD_REQUEST)

    # GET: api/v100/locations/country/select_list/
    @action(
        detail=False, methods=["get"], url_name="select_list", url_path="select_list"
    )
    def select_list(self, request):
        countries = country_services.get_active_country()
        if not countries:
            return Response(DATA_NOT_FOUND, status=status.HTTP_404_NOT_FOUND)
        serializer = ListSerializer(countries, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)