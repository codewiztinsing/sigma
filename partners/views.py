from django.shortcuts import render

from .models import PartnerCategory, PartnershipOpportunity


def partners(request):
    categories = PartnerCategory.objects.filter(is_active=True)
    return render(request, 'partners.html', {
        'active_page': 'partners',
        'partner_categories': categories,
    })


def partner(request):
    opportunities = PartnershipOpportunity.objects.filter(is_active=True)
    return render(request, 'partner.html', {
        'active_page': 'partner',
        'partnership_opportunities': opportunities,
    })
