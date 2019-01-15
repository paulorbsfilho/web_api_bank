from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = (
            'owner',
            'balance',
            'creation_date',
        )

        validators = [
            UniqueTogetherValidator(
                queryset=Account.objects.all(),
                fields=('owner',)
            )
        ]
