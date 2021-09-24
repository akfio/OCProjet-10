from django.contrib.auth.models import User
from rest_framework import serializers
from projects.models import Projects, Issues, Contributors, Comments


class ProjectSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'


class IssueSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Issues
        fields = '__all__'


class ContributorSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Contributors
        fields = '__all__'


class CommentSerialiser(serializers.ModelSerializer):

    class Meta:
        model = Comments
        fields = '__all__'


class UserSerialiser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
