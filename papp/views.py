from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import ContactMessage
from .forms import ContactMessageForm
from django.contrib.auth import authenticate, login,logout

def home(request):
    return render(request, "papp/index.html")
def about(request):
    return render(request, "papp/about.html")
def contact(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Message has been sent Successfully')
       
            
            return redirect('home')  
    else:
        form = ContactMessageForm()

    return render(request, 'papp/contact.html', {'form': form})
def portfolio(request):
    return render(request, "papp/portfolio.html")
def service(request):
    return render(request, "papp/service.html")
def team(request):
    return render(request, "papp/team.html")


from django.shortcuts import render
from .models import ContactMessage  # Make sure to import the model

@login_required
def message(request):
    # Assuming there is a model `ContactMessage` that stores messages related to the user
    add = ContactMessage.objects.all()
    return render(request, 'papp/client.html', {'userdata': add})
@login_required
def logout_user(request):

    logout(request)
    return redirect('home')