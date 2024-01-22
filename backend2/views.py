from rest_framework import viewsets
from .models import GolfCourse, Scorecard
from .serializers import GolfCourseSerializer, ScorecardSerializer

class GolfCourseViewSet(viewsets.ModelViewSet):
    queryset = GolfCourse.objects.all()
    serializer_class = GolfCourseSerializer

class ScorecardViewSet(viewsets.ModelViewSet):
    queryset = Scorecard.objects.all()
    serializer_class = ScorecardSerializer