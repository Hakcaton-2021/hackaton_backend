from django.urls import path
from hackaton.apps.business.views import CreateUnionsApiView

urlpatterns = [
    path('unions/', CreateUnionsApiView.as_view(), name="create-unions"),
]


