from rest_framework import serializers
from .models import Exploit

class ExploitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exploit
        fields = '__all__'
