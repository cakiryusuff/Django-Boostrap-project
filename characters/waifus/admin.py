from django.contrib import admin
from .models import Waifus
class WaifusAdmin(admin.ModelAdmin):
    list_display = ("id","name","created_date",)
    list_display_links = ("id","name",)
    search_fields = ("name","description",)

admin.site.register(Waifus,WaifusAdmin)