from django.shortcuts import render, redirect
from store.models.products import Product
from store.models.category import Category
from store.models.slider import Slider
from django.views import View

class Index(View):
    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity==1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity-1
                else:
                    cart[product] = quantity+1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        request.session['cart'] = cart
        print(request.session['cart'])
        return redirect('homepage')

    def get(self, request):
        slide = Slider.get_all_sliders()
        prod = None
        cat = Category.get_all_categories()
        categoryID = request.GET.get('category')
        if categoryID:
            prod = Product.get_all_products_by_categoryid(categoryID)
        else:
            prod = Product.get_all_products()
        data = {}
        data['sliders'] = slide
        data['products'] = prod
        data['categories'] = cat
        print('you are :',request.session.get('email'))
        return render(request, 'index.html' , data)

    #def get(self, request):
        #sld = None
        #sld = Slider.get_all_sliders()
       # print(sld)
        #return render(request, 'index.html' , {'sliders':sld})