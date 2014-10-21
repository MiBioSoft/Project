from django.contrib import admin
from django.db import models
from databasemodels.forms import UserForm, ProtocolForm
# Register your models here.

from databasemodels.models import User, Protocol, UserDescription

admin.site.register(UserDescription)
admin.site.register(Protocol)
