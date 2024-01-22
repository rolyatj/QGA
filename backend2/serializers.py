from rest_framework import serializers
from .models import GolfCourse, Scorecard

class GolfCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = GolfCourse
        fields = '__all__'

class ScorecardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scorecard
        fields = '__all__'