from django.contrib import admin
from app.models import *

admin.sites.AdminSite.site_header = "Systemd Online"
admin.sites.AdminSite.site_title = "Admin Dashboard"
admin.sites.AdminSite.index_title = "Systemd Online"

@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    search_fields = ('oper_id', )
    readonly_fields = ('_id', 'ctime', 'utime', )


@admin.register(Config)
class ConfigtAdmin(admin.ModelAdmin):
    search_fields = ('oper_id', )
    readonly_fields = ('ctime', 'utime', )


@admin.register(ServiceConfig)
class ServiceConfigAdmin(admin.ModelAdmin):
    list_filter = ('is_use', )
    search_fields = ('cname',)
    readonly_fields = ('ctime', 'utime',)


@admin.register(ConfigTemplate)
class ConfigTemplateAdmin(admin.ModelAdmin):
    search_fields  = ('name', 'owner_id', )
    readonly_fields = ('_id', 'ctime', 'utime', )


@admin.register(LogItem)
class LogItemAdmin(admin.ModelAdmin):
    readonly_fields = ('_id', 'ctime', 'oper_id', 'utime', )


@admin.register(Operator)
class OperatorAdmin(admin.ModelAdmin):
    readonly_fields = ('ctime', 'utime', )
    search_fields = ('domain', 'name', 'no', 'email', 'email_backup', 'phone', 'username',)

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    search_fields = ('synopsis', 'name', )
    readonly_fields = ('_id', 'ctime', 'utime', )


@admin.register(OperatorGroupRef)
class OperatorGroupRefAdmin(admin.ModelAdmin):
    pass

