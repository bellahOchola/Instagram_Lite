from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from lite.forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login
from .models import Image

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

    return render(request, 'index.html')


