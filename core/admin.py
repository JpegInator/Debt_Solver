from django.contrib import admin

from .models import CreditCard, PaymentSchedule, CalculationHistory

@admin.register(CreditCard)
class CreditCardAdmin(admin.ModelAdmin):
    list_display = ['name', 'credit_limit', 'interest_rate', 'current_debt']
    search_fields = ['name']

@admin.register(PaymentSchedule)
class PaymentScheduleAdmin(admin.ModelAdmin):
    list_display = ['card', 'month', 'payment_amount', 'remaining_debt']
    list_filter = ['card']

@admin.register(CalculationHistory)
class CalculationHistoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at', 'total_overpayment', 'payoff_months']
    list_filter = ['created_at']