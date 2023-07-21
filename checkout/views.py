from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51NDuTjLsB8Pejk6gQN3hr3C16UxtN2HXsutuSM7A7kb80UVfSLnxAAbYxiUWqZ9Y8D8dBk0pdXa95x3lClrbhefR00lzF1okmn',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
