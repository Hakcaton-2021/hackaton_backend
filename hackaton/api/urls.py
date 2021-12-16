from rest_framework import routers

from hackaton.api.v100.locations.views.comuna import ComunaViewSet

# Views
from hackaton.api.v100.locations.views.country import CountryViewset
from hackaton.api.v100.business.views.company import CompanyViewset

# Endpoint
router = routers.SimpleRouter()
router.register(r"v100/locations/country", CountryViewset, basename="v100-locations")
router.register(r"v100/locations/comuna", ComunaViewSet, basename="v100-locations")
router.register(r"business/company", CompanyViewset, basename="v100-business")


urlpatterns = router.urls
