from rest_framework import serializers


class Coin(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=