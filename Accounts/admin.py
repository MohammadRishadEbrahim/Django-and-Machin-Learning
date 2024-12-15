from django.contrib import admin
from .models import Camera , Contact ,Security

# Register your models here.
@admin.register(Camera)
class CameraAdmin(admin.ModelAdmin):
    list_display = ["Name","Active"]



@admin.register(Security)
class SecurityAdmin(admin.ModelAdmin):
    list_display = ["Name","Email","Phone","Status"]

    def get_status_display(self,obj):
        return obj.get_status_display()
    get_status_display.short_description = "Status"

    
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["Name","Email","Subject"]

