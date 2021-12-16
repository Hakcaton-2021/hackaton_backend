from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from hackaton.apps.forms.usecase import CreateFormCase
from hackaton.apps.forms.repository import FormRepository
from hackaton.apps.forms.serializers import FormSerializers
from rest_framework.exceptions import ValidationError
from django.views.generic import TemplateView
from hackaton.settings.base import URL


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
        except ValueError as e:
            raise ValidationError(detail={"email": e})


class ContactFormView(TemplateView):
    http_method_names = ["get", ]
    template_name = "contact_form.html"


class ContactFormView(TemplateView):
    http_method_names = ["get", ]
    template_name = "contact_form.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["base_url"] = URL
        return context