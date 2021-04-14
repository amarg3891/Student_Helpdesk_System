from django.contrib import admin
from .models import User
from .models import StudentCourse,StudentSyllabus
from .models import StudentSyllabus

admin.site.register(StudentCourse)
admin.site.register(StudentSyllabus)
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name','email','address','contact','course')