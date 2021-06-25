import stripe
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.conf import settings
from tienda.models import Tienda

# Create your views here
stripe.api_key = settings.STRIPE_TEST_SECRET_KEY
class OrdersPageView(TemplateView):
    model = Tienda
    template_name = 'orders/purchase.html'
    context_object_name = "productos"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stripe_key'] = settings.STRIPE_TEST_PUBLISHABLE_KEY
        return context

def charge(request):
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount = 600,
            currency = 'usd',
            description = 'Compra de articulo',
            source = request.POST['stripeToken']
        )
    return render(request,'orders/charge.html')