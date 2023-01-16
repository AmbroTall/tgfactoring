from rest_framework import serializers
from .models import BusinessInfo

class LoanSerializer(serializers.ModelSerializer):
    # bank_statement1 = serializers.FileField()
    # bank_statement2 = serializers.FileField()
    # bank_statement3 = serializers.FileField()
    class Meta:
        model = BusinessInfo
        # fields = ('loan_amount','period_to_receive_funds','what_for','monthly_revenue','credit_score','period_in_business','name','business_name','email','phone','bank_statement1','bank_statement2','bank_statement3',)
        fields = '__all__'