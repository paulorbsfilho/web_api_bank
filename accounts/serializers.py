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

    def validate_negative_balance(self, balance):
        if balance < 0:
            raise serializers.ValidationError("Your balance cant\'t be negative.")
        return balance

    def validate_manual_date(self, date):
        if date != "":
            raise serializers.ValidationError("You cant\'t set a date.")
        return date