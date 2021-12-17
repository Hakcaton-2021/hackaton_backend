from rest_framework import status, viewsets
from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import (
    AllowAny,
    DjangoModelPermissions,
    IsAdminUser,
    IsAuthenticated,
)
from rest_framework.response import Response

from hackaton.api.v100.business.serializers.company import (
    CreateSerializer,
    ListSerializer,
    UpdateSerializer,
)
from hackaton.apps.business.services import company as company_services
from hackaton.utils.lib.constants import DATA_NOT_FOUND, SERVER_ERROR


class CompanyViewset(viewsets.ViewSet):

    permission_classes = [AllowAny]
    # GET

    def list(self, request):
        company = company_services.get_all_companies()
        serializer = ListSerializer(company, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # POST
    def create(self, request):
        serializer = CreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                data={"message": "Razón Social creada correctamente."}, status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # GET: api/v100/business/company/<pk>/
    def retrieve(self, request, pk):
        if not pk:
            return Response(DATA_NOT_FOUND, status=status.HTTP_404_NOT_FOUND)
        company = company_services.get_company_by_pk(pk=pk)
        if not company:
            return Response(DATA_NOT_FOUND, status=status.HTTP_404_NOT_FOUND)
        serializer = ListSerializer(company)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # PUT: api/v100/business/company/<pk>/
    def update(self, request, pk):
        if not pk:
            return Response(DATA_NOT_FOUND, status=status.HTTP_404_NOT_FOUND)
        company = company_services.get_company_by_pk(pk=pk)
        if not company:
            return Response(DATA_NOT_FOUND, status=status.HTTP_404_NOT_FOUND)
        serializer = UpdateSerializer(company, data=request.data)
        if serializer.is_valid():
            serializer.save(update_fields=[
                "business_rut",
                "business_name",
                "business_giro",
                "business_direction",
                "business_phone",
                "representative_name",
                "representative_rut",
                "representative_email",
                "billing_rut",
                "type",
                "form",
                "gratification",
                "country",
                "mutual",
                "mutual_amount",
                "parent",
                "checking_account",
                "checking_bank",
                "payment_mobilization",
                "updated_at",
            ])
            return Response(
                data={"message": "Empresa actualizada con exito"},
                status=status.HTTP_200_OK,
            )
        return Response(SERVER_ERROR, status=status.HTTP_400_BAD_REQUEST)
