from django.contrib.auth import password_validation
from django.contrib.auth.hashers import check_password
from rest_framework import serializers


from .models import User


# pylint: disable=abstract-method
class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[password_validation.validate_password])
    balance = serializers.DecimalField(read_only=True, max_digits=15, decimal_places=2, coerce_to_string=False)

    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'balance')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)





class ResetPasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[password_validation.validate_password])

    class Meta:
        model = User
        fields = ('password', )

    def update(self, instance, validated_data):
        instance.set_password(validated_data.get('password'))
        instance.reset_password_token = None
        instance.save()
        return instance


class ChangePasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True, validators=[password_validation.validate_password])

    class Meta:
        model = User
        fields = ('password', 'old_password')

    def update(self, instance, validated_data):
        instance.set_password(validated_data.get('password'))
        instance.save()
        return instance

    def validate_old_password(self, value):
        if not check_password(value, self.instance.password):
            raise serializers.ValidationError('Invalid old password')
        return value
