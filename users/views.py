from django.shortcuts import render, redirect
from .forms import UserRegisterForm, ProfileUpdateForm, UserUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'تم بنجاح إنشاء حساب  {username} !')
            return redirect('blog:blog-home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form, 'title': 'register'})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if p_form.is_valid() and u_form.is_valid():
            p_form.save()
            u_form.save()
            messages.success(request, f'تم التعديل')
            return redirect('users:users-profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        

    context = {
        'u_form':u_form,
        'p_form':p_form,
        'title':f'{request.user.username} Profile'
    }
    return render(request, 'users/profile.html', context)


def author_profile(request, id):
    author = User.objects.get(id=id)
    profile = author.profile
    context = {
        'author':author,
        'profile':profile,
        'title': f'{author.username} profile'
    }
    return render(request, 'users/author_profile.html', context)