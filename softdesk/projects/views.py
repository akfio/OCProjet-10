from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, generics

from .models import Projects, Issues, Comments, Contributors
from .serializers import ProjectSerialiser, IssueSerialiser, CommentSerialiser, ContributorSerialiser
from rest_framework import permissions


class AuthorPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.author_user_id == request.user


class ProjectViewSet(viewsets.ModelViewSet):
    permission_classes = [AuthorPermission]

    queryset = Projects.objects.all()
    serializer_class = ProjectSerialiser

    def get_queryset(self):
        author = self.queryset.filter(author_user_id=self.request.user)
        contribution = self.queryset.filter(contributor=self.request.user)
        if author.exists() == True and contribution.exists() == True:
            return author and contribution
        elif author.exists() == True and contribution.exists() == False:
            return author
        elif author.exists() == False and contribution.exists() == True:
            return contribution

    def perform_create(self, serializer_class):
        serializer_class.save(author_user_id=self.request.user)


class IssueViewSet(viewsets.ModelViewSet):
    permission_classes = [AuthorPermission]

    queryset = Issues.objects.all()
    serializer_class = IssueSerialiser

    def get_queryset(self):
        project = self.queryset.filter(project_id=self.kwargs["project_pk"])
        return project

    def perform_create(self, serializer_class):
        projet = Projects.objects.get(project_id=self.kwargs["project_pk"])
        # contributor = Contributors.objects.get(user_id=self.request.user, project_id=projet)
        serializer_class.save(project_id=projet, author_user_id=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = [AuthorPermission]

    queryset = Comments.objects.all()
    serializer_class = CommentSerialiser

    def get_queryset(self):
        issue = self.queryset.filter(issue_id=self.kwargs["issue_pk"])
        return issue

    def perform_create(self, serializer_class):
        issue = Issues.objects.get(issue_id=self.kwargs["issue_pk"])
        serializer_class.save(issue_id=issue, author_user_id=self.request.user)


class ContributorViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = Contributors.objects.all()
    serializer_class = ContributorSerialiser

    def get_queryset(self):
        contributor = self.queryset.filter(project_id=self.kwargs["project_pk"])
        return contributor

    def perform_create(self, serializer_class):
        projet = Projects.objects.get(project_id=self.kwargs["project_pk"])
        serializer_class.save(project_id=projet)
