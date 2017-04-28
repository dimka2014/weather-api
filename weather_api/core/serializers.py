import json
from rest_framework import serializers


class RawJSONField(serializers.Field):
    def to_internal_value(self, obj):
        return json.dumps(obj)

    def to_representation(self, value):
        return json.loads(value)
