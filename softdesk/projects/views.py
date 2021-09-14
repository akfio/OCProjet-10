from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from .models import Projects, Issues, Comments, Contributors
from .serializers import ProjectSerialiser, IssueSerialiser, CommentSerialiser, ContributorSerialiser


class ProjectViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = Projects.objects.all()
    serializer_class = ProjectSerialiser


class IssueViewSet(viewsets.ModelViewSet):
    #permission_classes = (IsAuthenticated,)

    queryset = Issues.objects.all()
    serializer_class = IssueSerialiser


class CommentViewSet(viewsets.ModelViewSet):
    #permission_classes = (IsAuthenticated,)

    queryset = Comments.objects.all()
    serializer_class = CommentSerialiser


class ContributorViewSet(viewsets.ModelViewSet):
    #permission_classes = (IsAuthenticated,)

    queryset = Contributors.objects.all()
    serializer_class = ContributorSerialiser
