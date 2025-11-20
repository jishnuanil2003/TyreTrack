from rest_framework import serializers
from .models import BillModel

class BillSerializers(serializers.ModelSerializer):
    
    quantity = serializers.IntegerField(required=False, allow_null=True)

    def to_internal_value(self, data):
        # convert empty string "" to None before DRF validation
        if data.get("quantity") == "":
            data["quantity"] = None
        return super().to_internal_value(data)

    class Meta:
        model = BillModel
        fields = '__all__'
        extra_kwargs = {
            "tyre_name": {"required": False, "allow_null": True, "allow_blank": True},
            "tyre_size": {"required": False, "allow_null": True, "allow_blank": True},
            "quantity":  {"required": False, "allow_null": True},
        }