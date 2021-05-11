from django.shortcuts import render
from django.views.generic import (
    FormView,
    ListView,
    DetailView,
    View,
)
from django.shortcuts import render, HttpResponse
from deposit.models import Deposit
from deposit.forms import DepositForm


class DepositListView(ListView):

    model = Deposit
    template_name = 'deposit_list.html'


class DepositDetailView(DetailView):

    model = Deposit
    template_name = 'deposit_detail.html'


class NewDepositView(FormView):

    form_class = DepositForm
    template_name = 'form.html'
    success_url = '/'

    def form_valid(self, form):
        form.save()

        response = super().form_valid(form)

        return response




