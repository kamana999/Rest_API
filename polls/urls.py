from django.urls import path, include
from . import views
from .views import UserSet, StudentSet, CollegeSet, DemoView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('user',UserSet)
router.register('student', StudentSet)
router.register('college', CollegeSet)

app_name = 'polls'
urlpatterns = [
    path('', include(router.urls)),
    path('demo/',DemoView.as_view()),
    path('', views.index, name="index"),
    path('<int:id>/', views.detail, name="detail"),
    


]