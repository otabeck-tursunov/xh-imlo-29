from django.contrib import admin
from .models import *


class IncorretInline(admin.StackedInline):
    model = Incorrect
    extra = 1


class CorrectAdmin(admin.ModelAdmin):
    inlines = (IncorretInline,)


admin.site.register(Correct, CorrectAdmin)
admin.site.register(Incorrect)
