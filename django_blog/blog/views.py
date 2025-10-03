from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .forms import UserEditForm

User = get_user_model()



def login(request):
    
    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('pswd', '')
        print(username, password)
        errors = []
        
        if not username:
            errors.append("username required")
        if not password:
            errors.append('Password is required') 
            
        if not errors:
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                redirect('/')
            else:
                errors.append("Invalid username or password.")
        
        context = {
            'errors': errors,
            'username': username,
        }
        return render(request, 'blog/login.html', context)
    
    return render(request, 'blog/login.html')

def register(request):
    
    return render(request, 'blog/register.html', )


def blogs(request):
    
    
    
    return render(request, 'blog/blogs.html', )


@login_required
def profile(request):
    user = request.user
    if request.user == "POST":
        form = UserEditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')
        
        else:
            form = UserEditForm(instance=user)
        
    
        context = {
            'form': form,
            'user': user,
        }
    context = {}
    return render(request, 'blog/profile.html', context)

