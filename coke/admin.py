from django.contrib import admin
from coke.models import Notice,Academic,Parent_Information,faculty

class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Notice)
admin.site.register(Academic)
admin.site.register(Parent_Information)
admin.site.register(faculty)



