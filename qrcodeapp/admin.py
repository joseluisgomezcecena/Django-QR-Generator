from django.contrib import admin
from django.utils.safestring import mark_safe

from qrcodeapp.models import QrCode, DjangoPartNumbers


# Register your models here.
class QrCodeAdmin(admin.ModelAdmin):

    #return image tag with img_url as the source
    def img_url(self, obj):
        return mark_safe('<img src="{url}" width="150" height="150" />'.format(url=obj.img_url))

    #set the column name
    img_url.short_description = 'Image'

    #set the columns to display
    list_display = ('work_order', 'part_number', 'quantity', 'img_url', 'created_at', 'updated_at')

    #set the columns to filter
    list_filter = ('work_order', 'part_number', 'quantity', 'created_at', 'updated_at')

    #set the columns to search
    search_fields = ('work_order', 'part_number', 'quantity', 'created_at', 'updated_at')

    #set the columns to edit
    list_editable = ('part_number', 'quantity')

    #set the columns to sort
    ordering = ('work_order', 'part_number', 'quantity', 'created_at', 'updated_at')

    #set the columns to be readonly
    readonly_fields = ('img_url', 'created_at', 'updated_at')





admin.site.register(QrCode, QrCodeAdmin)
admin.site.register(DjangoPartNumbers)
