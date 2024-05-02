from django.shortcuts import render, redirect, get_object_or_404
from .models import Quote, Category
from django.http import HttpRequest, HttpResponse
from typing import Dict


def index(request: HttpRequest) -> HttpResponse:
    categories: Category = Category.objects.all()
    quotes: Quote = Quote.objects.all().order_by("?")[:9]

    context: Dict = {"categories": categories, "quotes": quotes}

    return render(request, "index.html", context)


def cat_detail(request: HttpRequest, cat_id: int) -> HttpResponse:
    quotes: Quote = Quote.objects.filter(category_id=cat_id)

    return render(request, "cat_detail.html", {"quotes": quotes})

#handles the query for a specific quote
def quote(request: HttpRequest, q_id: int) -> HttpResponse:
    quote: Quote = get_object_or_404(Quote, pk=q_id)

    return render(request, "quote.html", {"quote": quote})
