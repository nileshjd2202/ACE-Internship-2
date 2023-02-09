from rest_framework import serializers
from .models import College


# Validators
def start_with_g(value):
    if value[0].lower() != 'g':
        raise serializers.ValidationError('Name should be start with G')

class CollegeSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=10)
    name = serializers.CharField(max_length=100, validators=[start_with_g])
    address = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return College.objects.create(**validated_data)

    def update(self, instance, validate_data):
        instance.code = validate_data.get('code', instance.code)
        instance.name = validate_data.get('name', instance.name)
        instance.address = validate_data.get('address', instance.address)
        instance.save()
        return instance

    # Field Level Validation
    def validate_code(self, value):
        if int(value) > 50:
            raise serializers.ValidationError('College Code Entry limit only 50.')
        return value

    # Object Level Validation
    def validate(self, data):
        nm = data.get('name')
        ad = data.get('address')
        if nm.lower() == 'government engineering college katch' and ad.lower() != 'katch':
            raise serializers.ValidationError('Address must be Katch')
        return data
