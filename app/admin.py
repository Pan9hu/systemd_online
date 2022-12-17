from django.contrib import admin
from app.models import *

@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    readonly_fields = ('_id', 'ctime', 'utime')


@admin.register(Config)
class ConfigtAdmin(admin.ModelAdmin):
    pass

@admin.register(ServiceConfig)
class ServiceConfigAdmin(admin.ModelAdmin):
    pass

@admin.register(ConfigTemplate)
class ConfigTemplateAdmin(admin.ModelAdmin):
    pass

@admin.register(LogItem)
class LogItemAdmin(admin.ModelAdmin):
    pass

@admin.register(Operator)
class OperatorAdmin(admin.ModelAdmin):
    pass

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    pass

@admin.register(OperatorGroupRef)
class OperatorGroupRefAdmin(admin.ModelAdmin):
    pass

