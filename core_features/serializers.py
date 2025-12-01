from rest_framework import serializers
from .models import Users,Preferences,Ingredients,WeeklyMealPlan

class UsersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'
        extra_kwargs = {
            "password" :{"write_only": True}
        }

class PreferencesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Preferences
        fields = '__all__'

class IngredientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients
        fields = "__all__"

class WeeklyMealPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeeklyMealPlan
        fields = "__all__"