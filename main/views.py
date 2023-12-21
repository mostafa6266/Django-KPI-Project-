from django.shortcuts import render, redirect , get_object_or_404
from .models import Data
from .forms import AddKPIForm , CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login



def custom_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            # Redirect to a success page.
            return redirect('/')  # Replace 'home' with the name of your home page view
        else:
            # Return an 'invalid login' error message.
            context = {'error_message': "Invalid credentials"}
            return render(request, 'login.html', context)

    # If the method is GET, display the login form.
    return render(request, 'login.html')



@login_required(login_url="/login/")
def home(request):
    if request.method == 'POST':
        form = AddKPIForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            points = form.cleaned_data['points']
            user.day_kpi += points  # Add the points to day_kpi
            user.save()
            return redirect('/')  # Redirect after POST
    else:
        form = AddKPIForm()

    # Get the highest KPIs and corresponding users
    highest_day_kpi_user = Data.objects.order_by('-day_kpi').first()
    highest_month_kpi_user = Data.objects.order_by('-month_kpi').first()
    highest_total_kpi_user = Data.objects.order_by('-total_kpi').first()

    employees = Data.objects.all()
    context = {
        'employees': employees,
        'form': form,
        'highest_day_kpi_user': highest_day_kpi_user,
        'highest_month_kpi_user': highest_month_kpi_user,
        'highest_total_kpi_user': highest_total_kpi_user,
    }

    return render(request, 'index.html', context)

@login_required(login_url="/login/")
def transfer_kpi(request):
    employees = Data.objects.all()
    for employee in employees:
        employee.month_kpi += employee.day_kpi  # Add day_kpi to month_kpi
        employee.day_kpi = 0  # Reset day_kpi
        employee.save()

    return redirect('/')

@login_required(login_url="/login/")
def transfer_month_kpi(request):
    employees = Data.objects.all()
    for employee in employees:
        employee.month_kpi = 0
        employee.save(update_total_kpi=False)
    return redirect('/')
@login_required(login_url="/login/")
def user_data(request, pk):
    userData = get_object_or_404(Data, pk=pk)
    responsibilities = userData.responsibilities.all()
    comments = userData.data_comments.all()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user  # assuming the user is logged in
            comment.data = userData
            comment.save()
            return redirect('user_data', pk=pk)  # redirect back to the same page
    else:
        comment_form = CommentForm()

    context = {
        'user_data': userData,
        'responsibilities': responsibilities,
        'comments': comments,
        'comment_form': comment_form,  # Pass the form to the template
    }
    return render(request, 'user_data.html', context)


