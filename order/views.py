from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CheckoutForm

class Checkout(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')
    
    def get(self, *args, **kwargs):
        form = CheckoutForm()
        context = {
            'form': form
        }
        return render(self.request, 'order/checkout.html', context)
    
    def post(self, *args, **kwargs):
        form = CheckoutForm(self.request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            return JsonResponse({'success': True, 'errors': None})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
