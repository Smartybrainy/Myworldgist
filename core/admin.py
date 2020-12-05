from django.contrib import admin
from .models import EmailList


class EmailListAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ('name',
                    'email_address',
                    'created_date',
                    'completed',
                    )
    list_filter = ['name']
    search_fields = ['name', 'email_address']


admin.site.register(EmailList, EmailListAdmin)
