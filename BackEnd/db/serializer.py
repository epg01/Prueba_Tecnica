from rest_framework import serializers

# Own models
from .models import Records

class RecordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Records
        fields = '__all__'