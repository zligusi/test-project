from django import template
from cart.models import Cart


register = template.library()


@register.simple_tag(takes_context=True)
def get_cart_count(context):
    request =['request']
    if not request.session.session_key:
        return 0 
      
    try:
        cart = Cart.objects.get(session_key=request.session.session_key)
        return cart.total_items
    except cart.DoesNotExist:
        return 0
    
 
@register.filter   
def multiply(value, arg):
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):
        return 0