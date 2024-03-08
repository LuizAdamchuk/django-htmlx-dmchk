from django.shortcuts import render
from.models import Product
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt


def check_product(request):
  product = request.GET.get('product', '')
  products = Product.objects.filter(name=product)

  return render(request, 'partials/htmlx_components/check_product.html', {'products':products, 'product': product})

def save_product(request):
  name = request.POST.get('product')
  price = _pipe_price_validation(request.POST.get('price', '10') )

  product = Product(name=name, price=price)

  products = Product.objects.filter(name=product)

  if ( not products.exists() ):
    product.save()

  products = Product.objects.all()
  return render(request, 'partials/htmlx_components/list_all_products.html', {'products': products} )

@csrf_exempt
@require_http_methods(['DELETE'])
def delete_product(request, id):
  product = Product.objects.get(id=id)

  product.delete()

  products = Product.objects.all()
  return render(request, 'partials/htmlx_components/list_all_products.html', {'products': products} )

# ----- Private Function ----- #

def _pipe_price_validation(price_str: str):
    try:
        price = float(price_str)
        if price < 0:
            raise ValueError("Número negativo não permitido")
        return price
    except ValueError as e:
        print(e)
        return 10.0 
