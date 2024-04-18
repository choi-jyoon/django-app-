from django.shortcuts import render

# Create your views here.
def index(request):
    user = request.user
    context = {
        'user':user
    }
    return render(request, 'mypage/index.html', context)