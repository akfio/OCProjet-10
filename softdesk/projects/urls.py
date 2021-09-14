from django.urls import path, include
from rest_framework import routers

from . import views

app_name = 'projects'

router = routers.DefaultRouter()
router.register(r'projects', views.ProjectViewSet)
router.register(r'project/<int:pk>/issues', views.IssueViewSet)
router.register(r'project/<int:pk>/issue/<int:pk>/comments', views.CommentViewSet)
router.register(r'project/<int:pk>/users', views.ContributorViewSet)


urlpatterns = [

    path('projects/', include(router.urls)),

]
