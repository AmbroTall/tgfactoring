from django.contrib import admin
from .models import Loans

# Register your models here.

class Loanss(admin.ModelAdmin):
    list_display = ('name', 'loan_amount', 'credit_score')
admin.site.register(Loans, Loanss)

admin.site.site_header = 'TGIFactoring Administration'
