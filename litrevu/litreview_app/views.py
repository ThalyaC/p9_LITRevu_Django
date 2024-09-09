from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from litreview_app.models import Review, Ticket
from . import forms

"""def homepage(request):
    return render(request, 'litreview_app/homepage.html')"""

def registration(request):
    return render(request, 'litreview_app/registration.html')

@login_required
def flow(request):
    #reviews = Review.objects.all()
    tickets = Ticket.objects.all() #08/09/24
    return render(request, 'litreview_app/flow.html', {'tickets': tickets})

@login_required #08/09/24
def ticket_create(request):
    form = forms.TicketForm()
    if request.method == 'POST':
        form = forms.TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            # enregistre que l'auteur est bien l'utilisateur connecté
            ticket.author = request.user
            # enregistre le ticket
            ticket.save()
            return redirect('home')
    return render(request, 'litreview_app/ticket_create.html', context={'form': form})

@login_required
def review_create(request):
    return render(request, 'litreview_app/review_create.html')

@login_required
def review_ticket_create(request):
    return render(request, 'litreview_app/review_ticket_create.html')

@login_required
def your_posts(request):
    return render(request, 'litreview_app/your_posts.html')

@login_required
def review_update(request):
    return render(request, 'litreview_app/review_update.html')

@login_required
def ticket_update(request):
    return render(request, 'litreview_app/ticket_update.html')

@login_required
def subscriptions(request):
    return render(request, 'litreview_app/subscriptions.html')

def user_update(request):
    return render(request, 'litreview_app/user_update.html')

