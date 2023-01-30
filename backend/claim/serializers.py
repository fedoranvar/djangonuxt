from claim.models import Claim
from rest_framework import serializers


class ClaimSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Claim
        # fields = ["title", "priority", "doc_type", "is_special"]
        fields =  '__all__'
