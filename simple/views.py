from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse
from simple.models import Offer


def index(request):
    return render(request, 'index.html')


def offers(request):
    offer_list = Offer.objects.order_by('id')
    output = ', '.join(
        [
            f'operation={o.operation}; '
            f'stock={o.stock}; '
            f'value={o.value}; '
            f'shares={o.shares}; '
            f'when={o.datetime}' for o in offer_list
        ]
    )
    template = loader.get_template('../templates/offers.html')
    context = {
        'offer_list': offer_list,
        'details': output
    }
    return HttpResponse(template.render(context, request))
    # return render(request, template_name='offers.html')


def offer_details(request, offer_id):
    offer = Offer.objects.get(id=offer_id)
    return HttpResponse(
        f"Offer id:  {offer.id}</br>"
        f"Date time: {offer.datetime}</br>"
        f"Stock id:  {offer.stock}</br>"
        f"Operation: {offer.operation}</br>"
        f"Value:     {offer.value}</br>"
        f"Shares:    {offer.shares}</br>"
        f"Broker id: {offer.broker}"
    )


def make_offer(request):
    pass
