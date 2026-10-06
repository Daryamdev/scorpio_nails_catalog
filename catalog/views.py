from django.shortcuts import render,get_object_or_404
from .models import Category, Product



def home (request):
    categories=Category.objects.all()
    products =Product.objects.all()



    context={
        
        'categories': categories,
        'products': products
    }


    return render(request, 'catalog/main.html', context)




def tops(request):
    products=Product.objects.filter(category__slug='top-coats')
    context={
        'products': products
    }
    return render(request, 'catalog/tops.html', context)




def bases(request):
    products=Product.objects.filter(category__slug='base-coats')
    context={
        'products':products
    }
    return render(request,'catalog/bases.html',context)



def gels(request):
    products=Product.objects.filter(category__slug='gels')
    context={
        'products':products

    }
    return render(request,'catalog/gels.html',context)



def gelpolish(request):
    products=Product.objects.filter(category__slug='gel-polishes')
    context={
        'products':products
    }
    return render(request,'catalog/gelpolish.html',context)


def description(request, pk):
    product = get_object_or_404(Product, pk=pk)  # Retrieve the product by primary key or return a 404 if not found 
    context = {
        'product': product
    }
    return render(request, 'catalog/description.html', context)