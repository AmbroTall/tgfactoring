from django.shortcuts import render,redirect
from django.views.generic import FormView
from django.contrib.auth.models import User
from django.views.generic import ListView,DetailView,DeleteView,CreateView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.urls import reverse_lazy
from .forms import RegisterForm , LoansForm
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

        partner_1 = request.POST.get('partner1_name', None)
        partner_2 = request.POST.get('partner2_name', None)
        partner_3 = request.POST.get('partner3_name', None)
        partner_4 = request.POST.get('partner4_name', None)
        partner_5 = request.POST.get('partner5_name', None)

        partner_1_percantage = request.POST.get('partner1_percent', None)
        partner_2_percantage = request.POST.get('partner2_percent', None)
        partner_3_percantage = request.POST.get('partner3_percent', None)
        partner_4_percantage = request.POST.get('partner4_percent', None)
        partner_5_percantage = request.POST.get('partner5_percent', None)

        partner_1_city = request.POST.get('partner1_city', None)
        partner_2_city = request.POST.get('partner2_city', None)
        partner_3_city = request.POST.get('partner3_city', None)
        partner_4_city = request.POST.get('partner4_city', None)
        partner_5_city = request.POST.get('partner5_city', None)

        partner_1_state = request.POST.get('partner1_state', None)
        partner_2_state = request.POST.get('partner2_state', None)
        partner_3_state = request.POST.get('partner3_state', None)
        partner_4_state = request.POST.get('partner4_state', None)
        partner_5_state = request.POST.get('partner5_state', None)

        partner_1_zip = request.POST.get('partner1_zip', None)
        partner_2_zip = request.POST.get('partner2_zip', None)
        partner_3_zip = request.POST.get('partner3_zip', None)
        partner_4_zip = request.POST.get('partner4_zip', None)
        partner_5_zip = request.POST.get('partner5_zip', None)

        partner_1_address = request.POST.get('partner1_address', None)
        partner_2_address = request.POST.get('partner2_address', None)
        partner_3_address = request.POST.get('partner3_address', None)
        partner_4_address = request.POST.get('partner4_address', None)
        partner_5_address = request.POST.get('partner5_address', None)

        partner_1_ss = request.POST.get('partner1_ss', None)
        partner_2_ss = request.POST.get('partner2_ss', None)
        partner_3_ss = request.POST.get('partner3_ss', None)
        partner_4_ss = request.POST.get('partner4_ss', None)
        partner_5_ss = request.POST.get('partner5_ss', None)

        partner_1_email = request.POST.get('partner1_email', None)
        partner_2_email = request.POST.get('partner2_email', None)
        partner_3_email = request.POST.get('partner3_email', None)
        partner_4_email = request.POST.get('partner4_email', None)
        partner_5_email = request.POST.get('partner5_email', None)

        partner_1_phone = request.POST.get('partner1_phone', None)
        partner_2_phone = request.POST.get('partner2_phone', None)
        partner_3_phone = request.POST.get('partner3_phone', None)
        partner_4_phone = request.POST.get('partner4_phone', None)
        partner_5_phone = request.POST.get('partner5_phone', None)

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
        ein_document = request.FILES.get('ein_document', None)
        articles_of_incorporation = request.FILES.get('articles_of_incorporation', None)
        operating_agreement = request.FILES.get('operating_agreement', None)
        business_license = request.FILES.get('business_license', None)
        insurance_document = request.FILES.get('insurance_document', None)
        name = f"{first} {last}"

        details = Loans.objects.create(user=request.user,loan_amount=loan_amount, period_to_receive_funds=period_to_receive_funds, what_for=what_for, monthly_revenue=monthly_revenue, credit_score=credit_score, period_in_business=period_in_business, name=name, bank_statement1=bank_statement1, bank_statement2=bank_statement2, bank_statement3=bank_statement3,business_legal_name=business_legal_name, business_dba_name=business_dba_name, industry_type=industry_type, gross_annual_sales=gross_annual_sales, use_of_proceeds=use_of_proceeds, federal_tax_id=federal_tax_id, state_of_incorporation=state_of_incorporation, type_of_business_entity=type_of_business_entity, business_start_date=business_start_date, merchant_email=merchant_email, open_cash_advance_or_loans=open_cash_advance_or_loans,open_bankruptcies=open_bankruptcies,tax_liens_or_judgements=tax_liens_or_judgements, business_address=business_address,business_city=business_city, business_state=business_state,business_zip=business_zip, physical_phone_number=physical_phone_number, owner_name=owner_name, title=title, ownership_percentage=ownership_percentage,preferred_contact=preferred_contact,ss=ss,dob=dob,owner_address=owner_address, owner_city=owner_city, owner_state=owner_state, owner_zip=owner_zip,ein_document=ein_document, articles_of_incorporation=articles_of_incorporation, operating_agreement=operating_agreement,business_license=business_license,insurance_document=insurance_document,partner_1=partner_1, partner_2=partner_2,partner_3=partner_3,partner_4=partner_4,partner_5=partner_5,partner_1_percantage=partner_1_percantage,partner_2_percantage=partner_2_percantage,partner_3_percantage=partner_3_percantage, partner_4_percantage=partner_4_percantage,partner_5_percantage=partner_5_percantage, partner_1_city=partner_1_city,partner_2_city=partner_2_city,partner_3_city=partner_3_city,partner_4_city=partner_4_city,partner_5_city=partner_5_city,partner_1_state=partner_1_state,partner_2_state=partner_2_state,partner_3_state=partner_3_state,partner_4_state=partner_4_state,partner_5_state=partner_5_state,partner_1_zip=partner_1_zip,partner_2_zip=partner_2_zip,partner_3_zip=partner_3_zip,partner_4_zip=partner_4_zip,partner_5_zip=partner_5_zip,partner_1_address=partner_1_address,partner_2_address=partner_2_address,partner_3_address=partner_3_address,partner_4_address=partner_4_address,partner_5_address=partner_5_address, partner_1_ss=partner_1_ss,partner_2_ss=partner_2_ss, partner_3_ss=partner_3_ss,partner_4_ss=partner_4_ss,partner_5_ss=partner_5_ss, partner_1_email=partner_1_email,partner_2_email=partner_2_email,partner_3_email=partner_3_email,partner_4_email=partner_4_email,partner_5_email=partner_5_email,partner_1_phone=partner_1_phone,partner_2_phone=partner_2_phone,partner_3_phone=partner_3_phone,partner_4_phone=partner_4_phone,partner_5_phone=partner_5_phone)
        details.save()
        # context['display'] = "Yes"
        return redirect("https://tgifactoring.com")
    return render(request, 'loan/loan_form.html', context)


class LoansView(LoginRequiredMixin,ListView):
    model = Loans
    template_name = 'loan/display_loans.html'
    context_object_name = 'loans'
    def get_context_data(self, **kwargs):
        context = super(LoansView, self).get_context_data(**kwargs)
        context['loans'] = context['loans'].filter(user=self.request.user).order_by('-date_created')
        context['count'] = context['loans'].all().count()
        return context
class UpdateLoanView(UpdateView):
    model = Loans
    fields = '__all__'
    template_name = 'loan/edit_form.html'
    success_url = reverse_lazy('loan:loans_view')

