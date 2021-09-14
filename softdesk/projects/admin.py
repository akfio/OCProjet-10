from django.contrib import admin
from projects.models import Contributors, Projects, Issues, Comments

"""
@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'password']
"""


@admin.register(Contributors)
class ContributorsAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'project_id', 'role']


@admin.register(Comments)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ['description', 'issue_id']


class CommentInlines(admin.TabularInline):
    model = Comments


@admin.register(Issues)
class IssuesAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'assignee_user_id']
    inlines = [CommentInlines]


class IssueInlines(admin.TabularInline):
    model = Issues


@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'type']
    inlines = [IssueInlines]
