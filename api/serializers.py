from rest_framework import serializers

from api.models import Student


def start_with_a(value):
    """Validators [Priority 1(HIGH) rather than
    `Field Level Validation` & `Object level validation`]
    """
    if value[0].lower() != "a" or value[0] != "A":
        raise serializers.ValidationError("Should be start with `a`")


class StudentSerializer(serializers.ModelSerializer):
    # roll = serializers.CharField(read_only=True)
    name = serializers.CharField(validators=[start_with_a])

    class Meta:
        model = Student
        fields = ["name", "roll", "city"]
        # read_only_fields = ["name", "roll"]
        # extra_kwargs = {"name": {"read_only": True}}

    # Field Level Validation
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError("Seat Full !!")
        return value

    # Object level validation
    def validate(self, data):
        nm = data.get("name")
        ct = data.get("city")
        print(f"validate Value {nm[0]} {ct[0]}")
        if nm[0].islower() or ct[0].islower():
            raise serializers.ValidationError("Can't enter lower case !!")
        return data


"""
class StudentSerializer(serializers.Serializer):
    # id = serializers.IntegerField()
    name = serializers.CharField(max_length=100, validators=[start_with_a])
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # instance == old data in DB
        # validated_data == new data from user updation
    
        instance.name = validated_data.get("name", instance.name)
        instance.roll = validated_data.get("roll", instance.roll)
        instance.city = validated_data.get("coty", instance.city)
        instance.save()
        return instance

    # Field Level Validation
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError("Seat Full !!")
        return value

    # Object level validation
    def validate(self, data):
        nm = data.get("name")
        ct = data.get("city")
        print(f"validate Value {nm[0]} {ct[0]}")
        if nm[0].islower() or ct[0].islower():
            raise serializers.ValidationError("Can't enter lower case !!")
        return data
"""
