from django.shortcuts import render
from .models import Products,Order
from django.core.paginator import Paginator
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
# Create your views here.

def about(request):

	return render(request,'shop/about.html')

def index(request):

	product_objects=Products.objects.all()

	item_name=request.GET.get('item_name')

	if item_name !='' and item_name is not None:
		product_objects=Products.objects.filter(title__icontains=item_name)

	paginator=Paginator(product_objects,4)
	page=request.GET.get('page')
	product_objects=paginator.get_page(page)

	context={
		'product_objects':product_objects
	}

	return render(request,'shop/index.html',context)

class ProductDetailView(DetailView):
	model=Products

@login_required
def checkout(request):

	if request.method == "POST":

		items = request.POST.get('items','')
		name = request.POST.get('name',"")
		email = request.POST.get('email',"")
		address = request.POST.get('address',"")
		city = request.POST.get('city',"")
		state = request.POST.get('state',"")
		zipcode = request.POST.get('zipcode',"")
		total = request.POST.get('total','')

		order = Order(items=items,name=name, email=email, address=address, city=city, state=state, zipcode =zipcode,total=total)
		order.save()


	return render(request,'shop/checkout.html')	
