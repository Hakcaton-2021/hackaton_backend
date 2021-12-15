from django.urls import include, path
from hackaton.apps.forms.views import FormApiView

urlpatterns = [
    path('create/', FormApiView.as_view(), name="create-form")
]


