from claim.models import Claim
from rest_framework import permissions, viewsets
from claim.serializers import  ClaimSerializer
#
#
class ClaimViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Claim.objects.all().order_by("-create_date")
    serializer_class = ClaimSerializer
    permission_classes = [permissions.IsAuthenticated]
