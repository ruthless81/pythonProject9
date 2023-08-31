from django.shortcuts import render
from .models import User

def user_detail(request, user_id):
    user = User.objects.get(pk=user_id)
    return render(request, 'user/user_detail.html', {'user': user})
