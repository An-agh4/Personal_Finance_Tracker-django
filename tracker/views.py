from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Income, Expense, Category
from .forms import IncomeForm, ExpenseForm
from django.db.models import Sum


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

    incomes = Income.objects.filter(user=request.user)
    expenses = Expense.objects.filter(user=request.user)

    total_income = incomes.aggregate(Sum('amount'))['amount__sum'] or 0
    total_expense = expenses.aggregate(Sum('amount'))['amount__sum'] or 0

    balance = total_income - total_expense

    context = {
        'income': incomes,
        'expense': expenses,
        'total_income': total_income,
        'total_expense': total_expense,
        'balance': balance
    }

    return render(request, 'profile.html', context)


@login_required
def add_income(request):

    categories = Category.objects.filter(type='income')

    if request.method == "POST":

        amount = request.POST['amount']
        category_id = request.POST['category']

        category = Category.objects.get(id=category_id)

        Income.objects.create(
            user=request.user,
            amount=amount,
            category=category
        )

        return redirect('profile')

    return render(request, "income.html", {"categories": categories})

@login_required
def add_expense(request):

    categories = Category.objects.filter(type='expense')

    if request.method == "POST":

        amount = request.POST['amount']
        category_id = request.POST['category']

        category = Category.objects.get(id=category_id)

        Expense.objects.create(
            user=request.user,
            amount=amount,
            category=category
        )

        return redirect('profile')

    return render(request, "expense.html", {"categories": categories})

@login_required
def charts(request):

    expenses = Expense.objects.filter(user=request.user)

    data = (
        expenses
        .values('category__name')
        .annotate(total=Sum('amount'))
    )

    labels = []
    values = []

    for item in data:
        labels.append(item['category__name'])
        values.append(item['total'])

    return render(request, "charts.html", {
        "labels": labels,
        "data": values
    })
