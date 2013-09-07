# Register your admin here.
from polls.models import *
from django.contrib import admin



admin.site.register(Poll, PollAdmin)
admin.site.register(Choice, ChoiceAdmin)
