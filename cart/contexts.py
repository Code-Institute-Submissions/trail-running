from django.shortcuts import get_object_or_404
from discounts.models import Product, Size 


def cart_contents(request):
    """
    Ensures that the cart contents are available when rendering
    every page
    """
    cart = request.session.get('cart', {})                      
    cart_items = []                                             
    total = 0
    product_count = 0

    for id, quantity in cart.items():     #!!    shoe_size                  
        product = get_object_or_404(Product, pk=id)
        total += quantity * product.price
        product_count += quantity
        size = get_object_or_404(Size, pk=id)
        cart_items.append({'id': id, 'quantity': quantity, 'size': size, 'product': product})
        
    return {'cart_items': cart_items, 'total': total, 'product_count': product_count} 