from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'golfcourses', views.GolfCourseViewSet)
router.register(r'scorecards', views.ScorecardViewSet)

urlpatterns = [
    path('', include(router.urls)),
]