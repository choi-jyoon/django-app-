from django.shortcuts import render, redirect
from .models import Cart
from seller.models import Food
from django.http.response import JsonResponse
from django.db.models.aggregates import Sum
from django.contrib.auth.decorators import login_required
# Create your views here.
# def order_index(request):
#     return render(request, 'order/order')
def order_detail(request, pk):
    context = {
        'object': Food.objects.get(pk=pk)
    }
    return render(request, 'order/order_detail.html', context)

def modify_cart(request):
    # 사용자가 카트에 담은 음식 수량 조정
    # 응답 : 새롭게 변경된 수량, 전체 카트 음식 수량
    
    user = request.user
    
    food_id = request.POST['foodId']
    food = Food.objects.get(pk=food_id)
    
    cart, created = Cart.objects.get_or_create(user = user, food = food)
    
    #수량 업데이트
    change_amount = int(request.POST['amountChange'])
    cart.amount += change_amount
    
    if cart.amount >0:
        cart.save()
        
    # '내' 가 주문한 전체 음식 개수
    # user에 있는 cart 의 amount 의 합
    totalQuantity = user.cart_set.aggregate(totalCount=Sum('amount'))['totalCount']
    # 이 '음식'의 선택 수량
    
    context = {
        'newQuantity': cart.amount,
        'totalQuantity': totalQuantity,
        'message':'성공',
        'success': True,
    }
    return JsonResponse(context)

@login_required
def cart(request):
    carts = Cart.objects.filter(user = request.user)
    totalQuantity = request.user.cart_set.aggregate(totalCount=Sum('amount'))['totalCount']
    total_price = carts.aggregate(total_price=Sum('food__price') * Sum('amount'))['total_price']
    
    context = {
        'object_list': carts,
        'total': totalQuantity,
        # 'price': price,
        'total_price': total_price,
    }
    return render(request, 'order/cart_detail.html', context)

@login_required
def cart_delete(request, pk):
    cart = Cart.objects.get(pk=pk)
    cart.delete()
    return redirect('order:cart')

@login_required
def cart_update(request, pk):
    cart = Cart.objects.get(pk=pk)
    cart.delete()
    return redirect('order:cart')