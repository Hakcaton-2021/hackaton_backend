from rest_framework import routers

# Views
# from chileboleta.api.v100.branchs.views.branch import BranchViewSet -> Ejemplo

# Endpoint
router = routers.SimpleRouter()
# router.register(r"v100/business/business", BusinessViewset, basename="v100-business") -> Ejemplo


urlpatterns = router.urls
