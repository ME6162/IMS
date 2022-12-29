from django.contrib import admin

# Register your models here.
from .models import Institute
from .models import User

admin.site.register(Institute)
admin.site.register(User)
