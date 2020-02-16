from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from shop.models import Products
from django.contrib.auth.models import User
from .models import Cart
from django.contrib.auth.decorators import login_required



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('index')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def new_cart(request,param1,param2):

    user=request.user
    product=Products.objects.filter(title=param2).first()
    cart_row=Cart.objects.filter(user=user).filter(product=product).first()

    if param1=='add':

        if cart_row is None:

            new_cart_row=Cart(user=user,product=product)
            new_cart_row.save()

        else:

            cart_row.quantity=cart_row.quantity+1
            cart_row.save()
            print("in the else")

    elif param1=='remove':

        cart_row.quantity=cart_row.quantity-1

        cart_row.save()

        if cart_row.quantity==0:

            cart_row.delete()

    if len(Cart.objects.filter(user=user))==0:
        empty=True
    else:
        empty=False

    return render(request,'users/cart.html',{'cart_items':Cart.objects.filter(user=user),'add':'add','remove':'remove','empty':empty})


