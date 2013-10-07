from django.contrib import admin
from management.models import Holidays,Prospective_student,Event,current_student,Exam_rule,Title

class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Holidays)
admin.site.register(Prospective_student)
admin.site.register(Event)
admin.site.register(current_student)
admin.site.register(Exam_rule)
admin.site.register(Title)



