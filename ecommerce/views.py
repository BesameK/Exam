import datetime
from django.core.paginator import Paginator, EmptyPage
from .forms import OrderForm, TicketForm, CreateUserForm
from django.shortcuts import render, redirect
from .models import Order, Ticket
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def home(request):
    return render(request, "Ecommerce/home.html")


@login_required(login_url='login')
def tickets(request):
    ticket_items = Ticket.objects.all()
    p = Paginator(ticket_items, 4)
    page_num = request.GET.get('page', 1)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    context = {
        "tickets": page,
    }
    return render(request, "Ecommerce/ticket.html", context)


# @login_required(login_url='login')
def index(request):
    return render(request, "Ecommerce/order.html", {
        "orders": Order.objects.all()
    })


@login_required(login_url='login')
def createOrder(request):
    form1 = OrderForm()
    form2 = TicketForm()
    if request.method == "POST":
        form1 = OrderForm(request.POST)
        form2 = TicketForm(request.POST)

        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2.save()
            return redirect('/')

    context = {'form1': form1, 'form2': form2, }
    return render(request, "Ecommerce/order_form.html", context)


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        form = CreateUserForm()
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')

    context = {'form': form, }
    return render(request, 'Ecommerce/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'Ecommerce/login.html', context)


@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login')
