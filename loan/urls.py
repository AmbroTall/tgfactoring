from django.contrib import admin
from django.urls import path
from .views import loans_form ,LoginView,RegisterView, LoansView, UpdateLoanView
from django.contrib.auth.views import LogoutView

app_name="loan"
urlpatterns = [
    path('', loans_form, name='loans_form'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page ='loan:login'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('credits/', LoansView.as_view(), name='loans_view'),
    path('update/<int:pk>', UpdateLoanView.as_view(), name='update_loan'),

]
