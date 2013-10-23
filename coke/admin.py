from django.contrib import admin
from coke.models import Notice
class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Notice)



