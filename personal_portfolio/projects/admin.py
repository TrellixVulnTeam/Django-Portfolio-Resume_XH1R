from django.contrib import admin
from projects.models import Project


admin.site.site_header = "Admin Control Panel"
admin.site.site_title = "Admin CP"
admin.site.index_title = "Settings"

# Register your models here.
class NewProjectAdmin(admin.ModelAdmin):
    pass

admin.site.register(Project, NewProjectAdmin)