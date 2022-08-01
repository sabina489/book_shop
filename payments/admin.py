from django.contrib import admin
from .models import (
    Payment,
    OnlinePayment,
)



class OnlinePaymentInline(admin.TabularInline):
    model = OnlinePayment
    extra = 0
    show_change_link = True


class OnlinePaymentAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = ('id', 'order', 'amount',
                    'status', 'created_at', 'updated_at')
    list_filter = ('status',)


admin.site.register(OnlinePayment, OnlinePaymentAdmin)

