from django.contrib import admin

from .models import Question, Choice

admin.site.site_header = 'Pollster Admin'
admin.site.site_title = 'Pollster Admin Area'
admin.site.site_index_title = 'Welcome to the Pollster Admin area'

# Register your models here.
# FARI will show up in the admin area localhost:8000/admin/

# as is, this just makes the choices and questions as separate; not questions associated with questions; we use TabularInLine to change that
# admin.site.register(Question)
# admin.site.register(Choice)


class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    #            need a comma at the end because it's a tuple, and each tuple element is a string and a dictionary object and each dictionary object value is a list or strings??
    #            [(name, dict()),(name, dict()),]
    fieldsets = [(None, {'fields': ['question_text']}), ('Date Information', {
        'fields': ['pub_date'], 'classes': ['collapse']}), ]

    inlines = [ChoiceInLine]


admin.site.register(Question, QuestionAdmin)
