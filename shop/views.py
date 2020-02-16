from django.shortcuts import render,redirect
from .models import Products,Order
from django.core.paginator import Paginator
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from users.views import Cart
from django.contrib import messages
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
		'product_objects':product_objects,
		'add':'add',
		'view':'view',
		'products':'products'
	}

	return render(request,'shop/index.html',context)

class ProductDetailView(DetailView):
	model=Products

@login_required
def checkout(request):
	user=request.user
	cart_items=Cart.objects.filter(user=user)
	total=0
	for item in cart_items:

		total += item.product.price * item.quantity

	if request.method == "POST":

		items=""

		for item in cart_items:
			items += item.product.title +" "+ str(item.quantity) + "\n"
			

		name = request.POST.get('name',"")
		email = request.POST.get('email',"")
		address = request.POST.get('address',"")
		city = request.POST.get('city',"")
		state = request.POST.get('state',"")
		zipcode = request.POST.get('zipcode',"")

		order = Order(items=items,name=name, email=email, address=address, city=city, state=state, zipcode =zipcode,total=total)
		order.save()
		messages.success(request, f'Your order has been successfully placed')
		print("Im innn")
		return redirect('index')
	return render(request,'shop/checkout.html',{'cart_items':cart_items,'total':total})	
        


	
