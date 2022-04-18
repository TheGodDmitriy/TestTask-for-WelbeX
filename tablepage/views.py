from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Table

def table(request, page_number=1):
    tables = Table.objects.get_queryset().order_by('id')
    current_page = Paginator(tables, 5)

    return render(request, "tablepage/index.html", {'tables' : current_page.page(page_number)})
