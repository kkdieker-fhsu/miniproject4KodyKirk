from django.contrib import admin
from .models import Endpoints, TrafficLog

admin.site.register(Endpoints)

#due to using a composite primary key, this table cannot be registered in admin
#admin.site.register(TrafficLog)
