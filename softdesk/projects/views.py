from rest_framework.permissions import IsAuthenticated, SAFE_METHODS
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
        contributor = Contributors.objects.get_or_create(user_id=self.request.user, project_id=projet)
        serializer_class.save(project_id=projet, author_user_id=self.request.user, assignee_user_id=contributor[0])


class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = Comments.objects.all()
    serializer_class = CommentSerialiser

    def get_queryset(self):
        issue = self.queryset.filter(issue_id=self.kwargs["issue_pk"])
        return issue

    def perform_create(self, serializer_class):
        issue = Issues.objects.get(issue_id=self.kwargs["issue_pk"])
        serializer_class.save(issue_id=issue, author_user_id=self.request.user)


class ContributorViewSet(viewsets.ModelViewSet):
    permission_classes = [AuthorPermission]

    queryset = Contributors.objects.all()
    serializer_class = ContributorSerialiser

    def get_queryset(self):
        query = Projects.objects.all()
        contributor = query.filter(contributor=self.request.user, project_id=self.kwargs["project_pk"])
        author = query.filter(author_user_id=self.request.user, project_id=self.kwargs["project_pk"])
        if author.exists():
            if contributor.exists():
                contribut = self.queryset.filter(project_id=self.kwargs["project_pk"])
                return contribut
            else:
                contribut = self.queryset.filter(project_id=self.kwargs["project_pk"])
                return contribut
        else:
            if contributor.exists():
                contribut = self.queryset.filter(project_id=self.kwargs["project_pk"])
                return contribut

    def perform_create(self, serializer_class):
        query = Projects.objects.all()
        author = query.filter(author_user_id=self.request.user, project_id=self.kwargs["project_pk"])
        if author.exists():
            projet = Projects.objects.get(project_id=self.kwargs["project_pk"])
            serializer_class.save(project_id=projet)
