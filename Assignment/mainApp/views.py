from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from django.views.generic import TemplateView
import pandas as pd
import io
from datetime import datetime


class SupermarketSaleViewSet(viewsets.ModelViewSet):
    serializer_class = SupermarketSaleSerializer
    #returns the top 60 elements to the query set
    queryset = SupermarketSale.objects.all()[:60]

class CsvUploader(TemplateView):
    template_name = 'csv_uploader.html'

    def post(self, request):
        context = {
            'messages': []
        }

        csv = request.FILES['csv']
        csv_data = pd.read_csv(
            io.StringIO(
                csv.read().decode("utf-8")
            )
        )
        
        for record in csv_data.to_dict(orient="records"):
            try:
                date_object = datetime.strptime(record['Date'], "%m/%d/%Y")
                SupermarketSale.objects.create(
                    invoice_id = record['Invoice ID'],
                    product_line = record['Product line'],
                    unit_price = record['Unit price'],
                    quantity = record['Quantity'],
                    tax = record['Tax 5%'],
                    total = record['Total'],
                    date = date_object,
                    time = record['Time']
                )
            except Exception as e:
                breakpoint()
                context['exceptions_raised'] = e


        return render(request, self.template_name, context)