from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Profile, Content, Like


# Create your views here.
from .forms import ProfileForm
from django.contrib.auth.forms import UserCreationForm

#Logging in
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            first_letter = user.first_name[0] if user.first_name else None
            print("First letter:", first_letter)
            return redirect('/')
        else:
            error = 'Invalid username or password.'
            return render(request, 'login.html', {'error': error})
    else:
        return render(request, 'login.html')
    

def signup_view(request):
    if  request.method == "POST":
        form = UserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.clean_password2())
            user.save()
            Profile.objects.create(user=user)
            return redirect('/')
    else:
        form = UserCreationForm()
    
    return render(request, 'signup.html', {'form': form,})

def profile(request, username):
    user = User.objects.get(username=username)
    return render(request, 'profile.html', {'user': user})

@login_required
def update_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile', request.user.username)
    else:
        form = ProfileForm(instance=request .user.profile)

    return render(request, 'update-profile.html', {'form': form})

@login_required
def upload_content(request):
    if request.method == 'POST':
        tweet = request.POST.get('tweet')
        media = request.FILES.get('media')

        if tweet:
            if media:
                content = Content.objects.create(owner = request.user, tweet=tweet, media=media)
            else:
                content = Content.objects.create(owner = request.user, tweet=tweet)
            content.save()

            return redirect('profile', request.user.username)
    
    else:
        tweet, media

    return redirect('/')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def like_content(request, content_id):
    content = get_object_or_404(Content, pk=content_id)
    like, liked = Like.objects.get_or_create(owner=request.user, content=content)
    if not liked:
        like.delete()
    return redirect('/')