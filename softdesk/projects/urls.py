from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from . import views

app_name = 'projects'

router = DefaultRouter()
router.register(r'projects', views.ProjectViewSet, basename="projects")

issue_router = routers.NestedSimpleRouter(router, r'projects', lookup='project')
issue_router.register(r'issues', views.IssueViewSet, basename="issues")

user_router = routers.NestedSimpleRouter(router, r'projects', lookup='project')
user_router.register(r'users', views.ContributorViewSet, basename="users")

comment_router = routers.NestedSimpleRouter(issue_router, r'issues', lookup='issue')
comment_router.register(r'comments', views.CommentViewSet, basename="comments")

urlpatterns = [

    path('', include(router.urls)),
    path('', include(issue_router.urls)),
    path('', include(user_router.urls)),
    path('', include(comment_router.urls)),
]
