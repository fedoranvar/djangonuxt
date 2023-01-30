from django.contrib import admin
from.models import Claim

class ClaimAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', ]
    search_fields = ['title']

admin.site.register(Claim, ClaimAdmin)
#
