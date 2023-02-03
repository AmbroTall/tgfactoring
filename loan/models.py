from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Loans(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	loan_amount = models.CharField(max_length=50)
	period_to_receive_funds = models.CharField(max_length=50)
	what_for= models.CharField(max_length=50, blank=True)
	monthly_revenue = models.CharField(max_length=50)
	credit_score = models.CharField(max_length=50)
	period_in_business = models.CharField(max_length=50)
	name = models.CharField(max_length=50)
	bank_statement1 = models.FileField(upload_to='documents', max_length=500)
	bank_statement2 = models.FileField(upload_to='documents', max_length=500)
	bank_statement3 = models.FileField(upload_to='documents', max_length=500)


	#new fields added
	business_legal_name = models.CharField(max_length=255)
	business_dba_name = models.CharField(max_length=255)
	industry_type = models.CharField(max_length=255)
	gross_annual_sales = models.FloatField()
	use_of_proceeds = models.CharField(max_length=255)
	federal_tax_id = models.CharField(max_length=255)
	state_of_incorporation = models.CharField(max_length=255)
	type_of_business_entity = models.CharField(max_length=255)
	business_start_date = models.DateField(max_length=255)
	merchant_email = models.EmailField()
	open_cash_advance_or_loans = models.CharField(max_length=3)
	open_bankruptcies = models.CharField(max_length=3)
	tax_liens_or_judgements = models.CharField(max_length=3)
	business_address = models.CharField(max_length=255)
	business_city = models.CharField(max_length=255)
	business_state = models.CharField(max_length=255)
	business_zip = models.CharField(max_length=255)
	physical_phone_number = models.CharField(max_length=255)

	owner_name = models.CharField(max_length=255)
	title = models.CharField(max_length=255)
	ownership_percentage = models.FloatField()

	partner_1 = models.CharField(max_length=255,blank=True, null=True)
	partner_2 = models.CharField(max_length=255,blank=True, null=True)
	partner_3 = models.CharField(max_length=255,blank=True, null=True)
	partner_4 = models.CharField(max_length=255,blank=True, null=True)
	partner_5 = models.CharField(max_length=255,blank=True, null=True)

	partner_1_percantage = models.CharField(max_length=255,blank=True, null=True)
	partner_2_percantage = models.CharField(max_length=255,blank=True, null=True)
	partner_3_percantage = models.CharField(max_length=255,blank=True, null=True)
	partner_4_percantage = models.CharField(max_length=255,blank=True, null=True)
	partner_5_percantage = models.CharField(max_length=255,blank=True, null=True)

	preferred_contact = models.CharField(max_length=255)
	ss = models.CharField(max_length=255)
	dob = models.DateField(max_length=255)
	owner_address = models.CharField(max_length=255)
	owner_city = models.CharField(max_length=255)
	owner_state = models.CharField(max_length=255)
	owner_zip= models.CharField(max_length=255)

	ein_document = models.FileField(upload_to='documents', max_length=500, blank=True, null=True)
	articles_of_incorporation = models.FileField(upload_to='documents', max_length=500, blank=True, null=True)
	operating_agreement = models.FileField(upload_to='documents', max_length=500, blank=True, null=True)
	business_license = models.FileField(upload_to='documents', max_length=500, blank=True, null=True)
	insurance_document = models.FileField(upload_to='documents', max_length=500, blank=True, null=True)

	date_created = models.DateTimeField(auto_now_add=True, blank=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = "Loan"
