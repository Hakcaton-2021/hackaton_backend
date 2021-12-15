from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from hackaton.apps.forms.usecase import CreateFormCase
from hackaton.apps.forms.repository import FormRepository
from hackaton.apps.forms.serializers import FormSerializers
from rest_framework.exceptions import ValidationError


class FormApiView(CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = FormSerializers
    
    @property
    def repository(self):
        return FormRepository()
    
    def perform_create(self, serializer):
        data = dict(serializer.validated_data)
        use_case = CreateFormCase(self.repository)
        use_case.set_params(data)
        try:
           serializer.instance = use_case.execute()
        except use_case.ValidationError as error:
            raise ValidationError(detail={"error": error})