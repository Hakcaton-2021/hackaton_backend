from rest_framework import status, viewsets
from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import (
    AllowAny,
    DjangoModelPermissions,
    IsAdminUser,
    IsAuthenticated,
)
from rest_framework.response import Response

from hackaton.api.v100.business.serializers.accounting_account import (
    CreateSerializer,
    ListSerializer,
    UpdateSerializer,
)
from hackaton.apps.business.services import accounting_account as accounting_account_services
from hackaton.utils.lib.constants import DATA_NOT_FOUND, SERVER_ERROR

class AccountingAccountViewset(viewsets.ViewSet):

    permission_classes = [AllowAny]
    # GET: api/business/accounting_account/
    def list(self, request):
        accounting_account = accounting_account_services.get_all_accounting_account()
        serializer = ListSerializer(accounting_account, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # POST: api/business/accounting_account/
    def create(self, request):
        serializer = CreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                data={"message": "Cuenta contable creada con exito"}, status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # GET:api/business/accounting_account/<pk>/
    def retrieve(self, request, pk):
        if not pk:
            return Response(DATA_NOT_FOUND, status=status.HTTP_404_NOT_FOUND)
        accounting_account = accounting_account_services.get_accounting_account_by_pk(pk=pk)
        if not accounting_account:
            return Response(DATA_NOT_FOUND, status=status.HTTP_404_NOT_FOUND)
        serializer = ListSerializer(accounting_account)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # PUT: api/business/accounting_account/<pk>/
    def update(self, request, pk):
        if not pk:
            return Response(DATA_NOT_FOUND, status=status.HTTP_404_NOT_FOUND)
        accounting_account = accounting_account_services.get_accounting_account_by_pk(pk=pk)
        if not accounting_account:
            return Response(DATA_NOT_FOUND, status=status.HTTP_404_NOT_FOUND)
        serializer = UpdateSerializer(accounting_account, data=request.data)
        if serializer.is_valid():
            serializer.save(update_fields=[
                "company",
                "name",
                "code",
                "updated_at",
            ])
            return Response(
                data={"message": "Cuenta contable actualizada con exito"},
                status=status.HTTP_200_OK,
            )
        return Response(SERVER_ERROR, status=status.HTTP_400_BAD_REQUEST)

