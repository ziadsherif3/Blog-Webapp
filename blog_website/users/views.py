from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
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
    
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=current_user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=current_user.profile)
        
        if u_form.is_valid and p_form.is_valid:
            u_form.save()
            p_form.save()
            messages.success(request, f'Profile updated successfully!')
            return redirect('profile')
        
    else:
        u_form = UserUpdateForm(instance=current_user)
        p_form = ProfileUpdateForm(instance=current_user.profile)
    
        context = {
            'posts': current_user.post_set.all(),
            'u_form': u_form,
            'p_form': p_form
        }
        
        return render(request, 'users/profile.html', context)
