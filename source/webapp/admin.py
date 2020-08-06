from django.contrib import admin
from webapp.models import Issue, Status,IssueType



class IssueAdmin(admin.ModelAdmin):
    list_filter = ('status', 'issue_type')
    list_display = ('pk', 'summary','description', 'status', 'issue_type')
    search_fields = ('summary',)


admin.site.register(Issue,IssueAdmin)
admin.site.register(Status)
admin.site.register(IssueType)