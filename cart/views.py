from django.shortcuts import render, redirect, reverse
from django.contrib import messages

# Create your views here.

def view_cart(request):
    """A View that renders the cart contents page"""
    return render(request, "cart.html")


def add_to_cart(request, id):
    if request.user.is_authenticated:

        if request.POST.get('quantity') and int(request.POST.get('quantity')) > 0:
            quantity = int(request.POST.get('quantity')) 
            if request.POST.get('size'):
                size = int(request.POST.get('size'))
                print(size)

            cart = request.session.get('cart', {})
            
            if id in cart:
                if request.POST.get('size'):
                    cart[id] = [int(cart[id][0]) + quantity, size] #                    cart[id] = int(cart[id]) + quantity + shoe_size
                else: 
                    cart[id] = int(cart[id]) + quantity
            else:
                if request.POST.get('size'):
                    size = (request.POST.get('size'))
                    cart[id] = cart.get(id, quantity) #  , size
                else:
                    cart[id] = cart.get(id, quantity)

            request.session['cart'] = cart
        else:
            messages.warning(request, 'You have to specify how many products you want to purchase.')
    else:
            messages.warning(request, 'You have to register first, before you can purchase our products.')
            
    return redirect(reverse('all_products'))

def adjust_cart(request, id):
    """Adjust the quantity of the specified product to the specified amount"""
    if request.user.is_authenticated:
        
        if request.POST.get('quantity') and int(request.POST.get('quantity')) > 0:
            quantity = int(request.POST.get('quantity'))
            cart = request.session.get('cart', {})

            if quantity > 0:
                cart[id] = quantity
            else:
                cart.pop(id)    # pop() is an inbuilt function in Python that removes and returns last value from the list or the given index value. Syntax : list_name.pop(index)

            request.session['cart'] = cart
        else:
            messages.warning(request, 'You have to specify how many products you want to purchase.')

    else:
           
            messages.warning(request, 'You have to register first, before you can purchase our products.')
            
    return redirect(reverse('view_cart'))

def delete_from_cart(request, id):
    cart = request.session.get('cart', {})
    if id in cart:
        del cart[id]
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))        

        