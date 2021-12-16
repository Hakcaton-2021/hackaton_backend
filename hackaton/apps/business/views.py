from django.shortcuts import render
from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView
from hackaton.apps.business.usecase import CreateUnionsCase, ListUnionsCase
from hackaton.apps.business.repositories import UnionsRepository, CompanyRepository
from hackaton.apps.business.serializers import FormUnionsSerializers, UnionsSerializers
from rest_framework.exceptions import ValidationError
from django.views.generic import TemplateView
from hackaton.settings.base import URL


class CreateUnionsApiView(ListCreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = FormUnionsSerializers
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return UnionsSerializers
        return FormUnionsSerializers
    
    @property
    def repository(self):
        return UnionsRepository()
    
    def get_queryset(self):
        use_case = ListUnionsCase(self.repository, CompanyRepository())
        try:
            unions = use_case.execute(self.request.GET.get('form_id'))
        except Exception as e:
            return []
        if unions:
            return unions
        return []
    
    def perform_create(self, serializer):
        data = dict(serializer.validated_data)
        use_case = CreateUnionsCase(self.repository, CompanyRepository())
        use_case.set_params(data)
        try:
           serializer.instance = use_case.execute()
        except use_case.ValidationError as error:
            raise ValidationError(detail={"error": error})
        return True