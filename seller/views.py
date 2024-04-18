from django.shortcuts import render, redirect
from .models import Food
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage

# Create your views here.
@login_required
def seller_index(request):
    food = Food.objects.all().filter(user__id=request.user.id)
    context = {
        'object_list' : food
    }
    return render(request, 'seller/seller_index.html', context)

@login_required
def add_food(request):
    if request.method == 'GET':
        return render(request, 'seller/seller_add_food.html')
    elif request.method == 'POST':
        # form에서 전달되는 각 값을 뽑아서 DB에 저장
        food_name = request.POST['name']
        food_price = request.POST['price']
        food_description = request.POST['description']
        
        fs=FileSystemStorage()
        uploaded_file = request.FILES['file']
        name = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(name)
        
        Food.objects.create(user = request.user, name=food_name, price =food_price, description = food_description, img_url = url)
        return redirect('seller:seller_index')
    
@login_required
def food_detail(request, pk):
    object=Food.objects.get(pk=pk)
    context = {
        'object' : object
    }
    return render(request, 'seller/seller_food_detail.html', context)

@login_required
def food_delete(request, pk):
    object=Food.objects.get(pk=pk)
    object.delete()
    return redirect('seller:seller_index')