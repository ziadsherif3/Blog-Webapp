from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from blog.models import Post
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
    if request.method == 'POST':
        reg_form = UserRegisterForm(request.POST)
        if reg_form.is_valid():
            reg_form.save()
            username = reg_form.cleaned_data.get('username')
            messages.success(request, f'Account created successfully!')
            return redirect('login')
            
    else:
        reg_form = UserRegisterForm()
    return render(request, 'users/register.html', {'reg_form': reg_form, 'title': 'Register'})

@login_required
def profile(request):
    current_user = request.user
    context = {
        'posts': current_user.post_set.all()
    }
    
    return render(request, 'users/profile.html', context)
