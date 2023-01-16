from django.shortcuts import render,redirect
from django.views.generic import FormView
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.urls import reverse_lazy
from .forms import RegisterForm
from .models import Loans
from django.contrib.auth.decorators import login_required


class LoginView(LoginView):
    fields = '__all__'
    template_name = 'loan/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('loan:loans_form')

class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'loan/register.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('loan:loans_form')


    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterView, self).form_valid(form)


    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('loan:loans_form')
        return super(RegisterView,self).get(*args, **kwargs)

@login_required
def loans_form(request):
    context = {}
    context['display'] = "No"
    if request.method == 'POST':
        loan_amount = request.POST['loan_amount']
        period_to_receive_funds = request.POST['period_to_receive_funds']
        what_for= request.POST['what_for']
        monthly_revenue = request.POST['monthly_revenue']
        credit_score = request.POST['credit_score']
        period_in_business = request.POST['period_in_business']
        first = request.POST["first"]
        last = request.POST["last"]
        bank_statement1 = request.FILES['bank_statement1']
        bank_statement2= request.FILES['bank_statement2']
        bank_statement3 = request.FILES['bank_statement3']

        business_legal_name = request.POST["business_legal_name"]
        business_dba_name = request.POST["business_dba_name"]
        industry_type = request.POST["industry_type"]
        gross_annual_sales = request.POST["gross_annual_sales"]
        use_of_proceeds = request.POST["use_of_proceeds"]
        federal_tax_id = request.POST["federal_tax_id"]
        state_of_incorporation = request.POST["state_of_incorporation"]
        type_of_business_entity = request.POST["type_of_business_entity"]
        business_start_date = request.POST["business_start_date"]
        merchant_email = request.POST["merchant_email"]
        open_cash_advance_or_loans = request.POST["open_cash_advance_or_loans"]
        open_bankruptcies = request.POST["open_bankruptcies"]
        tax_liens_or_judgements = request.POST["tax_liens_or_judgements"]
        business_address = request.POST["business_address"]
        business_city = request.POST["business_city"]
        business_state = request.POST["business_state"]
        business_zip = request.POST["business_zip"]
        physical_phone_number = request.POST["physical_phone_number"]
        owner_name = request.POST["owner_name"]
        title = request.POST["title"]
        ownership_percentage = request.POST["ownership_percentage"]
        preferred_contact = request.POST["preferred_contact"]
        ss = request.POST["ss"]
        dob = request.POST["dob"]
        owner_address = request.POST["owner_address"]
        owner_city = request.POST["owner_city"]
        owner_state = request.POST["owner_state"]
        owner_zip = request.POST["owner_zip"]
        ein_document = request.FILES['ein_document']
        articles_of_incorporation = request.FILES['articles_of_incorporation']
        operating_agreement = request.FILES['operating_agreement']
        business_license = request.FILES['business_license']
        insurance_document = request.FILES['insurance_document']
        name = f"{first} {last}"


        details = Loans.objects.create(loan_amount=loan_amount, period_to_receive_funds=period_to_receive_funds, what_for=what_for, monthly_revenue=monthly_revenue, credit_score=credit_score, period_in_business=period_in_business, name=name, bank_statement1=bank_statement1, bank_statement2=bank_statement2, bank_statement3=bank_statement3,business_legal_name=business_legal_name, business_dba_name=business_dba_name, industry_type=industry_type, gross_annual_sales=gross_annual_sales, use_of_proceeds=use_of_proceeds, federal_tax_id=federal_tax_id, state_of_incorporation=state_of_incorporation, type_of_business_entity=type_of_business_entity, business_start_date=business_start_date, merchant_email=merchant_email, open_cash_advance_or_loans=open_cash_advance_or_loans,open_bankruptcies=open_bankruptcies,tax_liens_or_judgements=tax_liens_or_judgements, business_address=business_address,business_city=business_city, business_state=business_state,business_zip=business_zip, physical_phone_number=physical_phone_number, owner_name=owner_name, title=title, ownership_percentage=ownership_percentage,preferred_contact=preferred_contact,ss=ss,dob=dob,owner_address=owner_address, owner_city=owner_city, owner_state=owner_state, owner_zip=owner_zip,ein_document=ein_document, articles_of_incorporation=articles_of_incorporation, operating_agreement=operating_agreement,business_license=business_license,insurance_document=insurance_document)
        details.save()
        # context['display'] = "Yes"
        return redirect("https://tgifactoring.com")
    return render(request, 'loan/loan_form.html', context)