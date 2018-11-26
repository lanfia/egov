from django.contrib import admin
from egov_ams.models import *


class AssetAdmin(admin.ModelAdmin):
    exclude = ['status',]
    fieldsets = (
        (None,{
            'fields': ('gsa_asset_code','asset_category','model_number','serial_number','procurement_date','asset_value','asset_image','note')

        }),
        ('Donor Asset Detail',{
            'classes': ('collapse',),
            'fields': ('donated','partner','donation_type'),
        }),
    )

admin.site.register(Asset, AssetAdmin)
admin.site.register(Category)
admin.site.register(Manufacturer)
admin.site.register(ManfacturerModel)
admin.site.register(Vehicle)
admin.site.register(VehicleType)
admin.site.register(AssetTransfer)
admin.site.register(VehicleTransfer)


class EmployeeAssetAssignedInline(admin.TabularInline):
    model = EmployeeAssetAssigned

admin.site.register(EmployeeAssetAssigned)


class AssetAssignedAdmin(admin.ModelAdmin):
    exclude = ['status']
    inlines = [
        EmployeeAssetAssignedInline,
    ]

class VehicleInventoryLogInline(admin.TabularInline):
    model = VehicleInventoryLog
    
admin.site.register(VehicleInventoryLog) 

admin.site.register(AssetAssigned, AssetAssignedAdmin)

class InventoryLogInline(admin.TabularInline):
    model = InventoryLog

admin.site.register(InventoryLog)

class InventoryAdmin(admin.ModelAdmin):
    
    
    inlines = [
        InventoryLogInline,
    ]
admin.site.register(Inventory, InventoryAdmin)

