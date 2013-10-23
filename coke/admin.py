from django.contrib import admin
from coke.models import Notice,Academic,Parent_Information

class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Notice)
admin.site.register(Academic)
admin.site.register(Parent_Information)



