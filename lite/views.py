from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from lite.forms import SignUpForm, LoginForm, UploadImage
from django.contrib.auth import authenticate, login
from .models import Image
from django.contrib.auth.models import User

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'registration/registration_form.html', {'form': form})

def index(request):
    all_captions = Image.get_captions()
    users = User.objects.exclude(id=request.user.id)
    if request.method == 'POST':
        form = UploadImage(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user.profile
            post.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = UploadImage()

    return render(request, 'index.html', {'form':form})


