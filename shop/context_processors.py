
from .models import Category
def cart_count(request):
    cart = request.session.get('cart', {})
    return {'cart_count': sum(cart.values())}


def categories_context(request):
    return {
        'categories': Category.objects.all()
    }
