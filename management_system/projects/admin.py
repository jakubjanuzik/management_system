from django.contrib import admin

# Register your models here.
from projects.models import Project, Role, Team


class MembershipInline(admin.TabularInline):
    model = Team.users.through


class TeamsAdmin(admin.ModelAdmin):
    inlines = [
        MembershipInline,
    ]


admin.site.register(Project)
admin.site.register(Role)
admin.site.register(Team, TeamsAdmin)
