from django.conf import settings
import stripe
from django.http import JsonResponse
from django.views import View
from django.views.generic import TemplateView, ListView

from .models import Item

stripe.api_key = settings.STRIPE_SECRET_KEY


class IndexPageView(ListView):
    model = Item
    template_name = 'payment/index.html'
    context_object_name = 'items'


class DetailPageView(TemplateView):
    template_name = 'payment/item.html'
    context_object_name = 'item'

    def get_context_data(self, **kwargs):
        item_id = self.kwargs['item_id']
        item = Item.objects.get(pk=item_id)
        context = {
            'item': item,
            'stripe_public_key': settings.STRIPE_PUBLIC_KEY
        }
        return context



class CreateCheckoutSessionView(View):
    def get(self, request, *args, **kwargs):
        item_id = self.kwargs['item_id']
        item = Item.objects.get(pk=item_id)
        checkout_session = stripe.checkout.Session.create(
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': item.name,
                    },
                    'unit_amount': item.price,
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=settings.YOUR_DOMAIN + 'success/' + '?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=settings.YOUR_DOMAIN + 'cancel/',
        )
        return JsonResponse({
            'id': checkout_session.id
        })


class SuccessView(TemplateView):
    template_name = 'payment/success.html'


class CancelView(TemplateView):
    template_name = 'payment/cancel.html'