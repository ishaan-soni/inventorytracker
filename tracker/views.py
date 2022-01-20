import sqlite3
from django.shortcuts import render, reverse
from .forms import ItemModelForm
from .models import Item
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, TemplateView
import pandas as pd


class ItemCreateView(CreateView):
    template_name = 'tracker/item_create.html'
    form_class = ItemModelForm

    def get_success_url(self): #after form saved successfully 
        return reverse('item-list')


class ItemListView(ListView):
    template_name = 'tracker/listview.html'
    queryset = Item.objects.all()
    context_object_name = 'items'


class ItemDetailView(DetailView):
    template_name = 'tracker/item_detail.html'
    queryset = Item.objects.all()
    context_object_name = 'item'

class ItemUpdateView(UpdateView):
    template_name = "tracker/item_update.html"
    form_class = ItemModelForm
    queryset = Item.objects.all()

    def get_success_url(self):
        return reverse('item-list')

class ItemDeleteView(DeleteView):
    template_name = 'tracker/item_delete.html'
    queryset = Item.objects.all()

    def get_success_url(self):
        return reverse('item-list')
    


# class CsvView(TemplateView):
#     df = pd.read_sql(sql='tracker_item',con=sqlite3)
#     df.to_csv('new_file.csv',index=False)
    







