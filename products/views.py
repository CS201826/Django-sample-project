from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from products.models import Category, Product
from products.forms import CategoryForm, ProductForm

class Home(TemplateView):
	template_name = 'home.html'

class CategoryList(ListView):
	model = Category
	template_name = 'category/list.html'

class CategoryCreate(CreateView):
	model = Category
	form_class = CategoryForm
	template_name = 'category/add.html'
	success_url = reverse_lazy('category-list')

class CategoryUpdate(UpdateView):
	model = Category
	form_class = CategoryForm
	template_name = 'category/edit.html'
	success_url = reverse_lazy('category-list')

class CategoryDelete(DeleteView):
	model = Category
	form_class = CategoryForm
	template_name = 'category/delete.html'
	success_url = reverse_lazy('category-list')

class ProductList(ListView):
	model = Product
	template_name = 'product/list.html'

class ProductCreate(CreateView):
	model = Product
	form_class = ProductForm
	template_name = 'product/add.html'
	success_url = reverse_lazy('product-list')

class ProductUpdate(UpdateView):
	model = Product
	form_class = ProductForm
	template_name = 'product/edit.html'
	success_url = reverse_lazy('product-list')

class ProductDelete(DeleteView):
	model = Product
	form_class = ProductForm
	template_name = 'product/delete.html'
	success_url = reverse_lazy('product-list')


		
