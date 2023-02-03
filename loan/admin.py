from django.contrib import admin
from .models import Loans
from django.contrib.admin import ModelAdmin

class Loanss(admin.ModelAdmin):
    list_display = ('name', 'loan_amount', 'credit_score')
    exclude = ('bank_statement1','bank_statement2','bank_statement3', 'id')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if not request.user.is_staff:
            qs = qs.exclude(restricted_field=True)
        return qs
admin.site.register(Loans, Loanss)

admin.site.site_header = 'TGIFactoring Administration'
