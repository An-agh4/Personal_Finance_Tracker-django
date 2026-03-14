from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Income, Expense, Category
from .forms import IncomeForm, ExpenseForm


def home(request):
    return render(request, "home.html")


def signup(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")

    return render(request, "signup.html", {"form": form})


@login_required
def profile(request):
    income = Income.objects.filter(user=request.user)
    expense = Expense.objects.filter(user=request.user)

    return render(request, "profile.html", {
        "income": income,
        "expense": expense
    })


@login_required
def add_income(request):

    if request.method == "POST":
        form = IncomeForm(request.POST)

        if form.is_valid():
            income = form.save(commit=False)
            income.user = request.user
            income.save()
            return redirect("profile")

    else:
        form = IncomeForm()

    return render(request, "income.html", {"form": form})


@login_required
def add_expense(request):

    if request.method == "POST":
        form = ExpenseForm(request.POST)

        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect("profile")

    else:
        form = ExpenseForm()

    return render(request, "expense.html", {"form": form})

@login_required
def charts(request):

    expenses = Expense.objects.filter(user=request.user)

    labels = []
    data = []

    for exp in expenses:
        labels.append(exp.category.name)
        data.append(exp.amount)

    return render(request, "charts.html", {
        "labels": labels,
        "data": data
    })
