from rest_framework import routers

from hackaton.api.v100.locations.views.comuna import ComunaViewSet

# Views
from hackaton.api.v100.locations.views.country import CountryViewset

# Endpoint
router = routers.SimpleRouter()
router.register(r"v100/locations/country", CountryViewset, basename="v100-locations")
router.register(r"v100/locations/comuna", ComunaViewSet, basename="v100-locations")


urlpatterns = router.urls
