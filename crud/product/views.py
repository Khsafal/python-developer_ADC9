from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import Template,Context
from .models import Product
# Create your views here.
def view_add_product(request):
    return render(request,'add_product.html')

def view_product_lists(request):
    list_of_products= Product.objects.all()
    context_variable = {
        'products':list_of_products
    }
    return render(request,'display_product.html',context_variable)


def view_productdata_save(request):
    if request.method == "POST":
        # get_all = request.POST
        get_name = request.POST['product_name']
        
        get_code = request.POST['product_code']
        get_price = request.POST['product_price']
        
        product_obj = Product(product_name=get_name,product_code=get_code,product_price=get_price)
        product_obj.save()
        return HttpResponse("Record saved")
    else:
        return HttpResponse("Error record saving")


def view_productdata_updateform(request,ID):
 
    product_obj = Product.objects.get(id=ID)
    
    context_varible = {
        'product':product_obj
    }
    return render(request,'update_product.html',context_varible)


def view_update_form_data_in_db(request,ID):
    product_obj = Product.objects.get(id=ID)
    
    product_form_data = request.POST
    
    product_obj.product_name = request.POST['product_name']
    product_obj.product_code =request.POST['product_code']
    product_obj.product_price = request.POST['product_price']
    product_obj.save()
    return HttpResponse("Record Updated!!")


def view_delete(request,ID):  
    product_obj = Product.objects.get(id=ID)  
    product_obj.delete()   
    return HttpResponse("deleted")