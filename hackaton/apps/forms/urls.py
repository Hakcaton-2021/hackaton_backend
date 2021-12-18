from django.urls import include, path
from hackaton.apps.forms.views import FormApiView, ContactFormView

urlpatterns = [
    path('create/', FormApiView.as_view(), name="create-form"),
    path('', ContactFormView.as_view(), name="read-form"),
]


