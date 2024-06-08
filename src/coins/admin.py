from django.contrib import admin
from .models import Job, Task, Output, Contract, OfficialLink, Social

# Register your models here.
admin.site.register(Job)
admin.site.register(Task)
admin.site.register(Output)
admin.site.register(Contract)
admin.site.register(OfficialLink)
admin.site.register(Social)
