from django.shortcuts import render
from store.models import Cart
from users.models import profile

def getcart(request):
    if not request.user.is_authenticated:
        return []
    else:
        Profile = profile.objects.get(user=request.user)
        return Cart.objects.get(user=Profile)


# Create your views here.
def index(request):
    global cart
    
    cart = getcart(request)
    return render(request, 'index.html', {'cart': cart})