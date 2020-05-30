from django.urls import path, include

from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register('courses', views.CourseViewSet)
router.register('subjects', views.SubjectViewSet)
router.register('modeles', views.ModuleViewSet)


app_name = 'courses'

urlpatterns = [
    # path("courses/<pk>/enroll/", views.CourseEnrollView.as_view(), name="course_enroll"),
    path("", include(router.urls)),
]
