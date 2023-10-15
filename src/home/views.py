from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from .forms import SignUpForm
from .models import Record


# Create your views here.
def home(request):
    records = Record.objects.all()

    # check if user is logged in
    if request.method=="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        # User authentication
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            messages.success(request, "Successfully logged in!")
            return redirect('home')
        else:
            messages.success(request, "Credentials invalid! Please try again.")
            return redirect('home')
    else:
        return render(request, 'home.html', {'records':records})

def login_user(request):
    pass

def logout_user(request):
    logout(request)
    messages.success(request, "You have been Logged out....")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # save user
            form.save()
            # get username
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, "Successfully registered!")
            return redirect('home')
        return render(request, 'register.html', {})
    else:
        form = SignUpForm()
        context = {'form':form}
        return render(request, 'register.html', context)
    
    return render(request, 'register.html', context)

def customer_record(request, pk):
	if request.user.is_authenticated:
		# Look Up Records
		customer_record = Record.objects.get(id=pk)
		return render(request, 'record.html', {'customer_record':customer_record})
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('home')
