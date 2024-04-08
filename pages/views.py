from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from users.models import Content

# Create your views here.

@login_required(login_url='login')
def Homepage(request):
    contents = Content.objects.all()
    return render(request, 'home.html', {'contents': contents, })


@login_required(login_url='login')
def user_profile(request, username):
    profile_user = get_object_or_404(User, username=username)
    contents = Content.objects.filter(owner=profile_user)
    return render(request, 'profile.html', {'contents': contents, 'profile_user': profile_user})
