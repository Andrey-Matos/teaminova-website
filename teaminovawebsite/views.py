from django.shortcuts import redirect, render
from django.contrib.auth.password_validation import validate_password, password_validators_help_texts
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
User = get_user_model()

def login_user(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        return render(request, "authenticate/login.html", {"error": "Invalid email or password."})
    else:
        return render(request, "authenticate/login.html", {})

@login_required
def home(request):
    return render(request, "home/home.html", {})

def register_user(request):
    errors = []
    current_user = User.objects.filter(email=request.POST["email"]).first()


    if current_user:
        errors.append("the given email is already being used")
    if request.POST["password"] != request.POST["confirmPassword"]:
        errors.append("passwords don't match")
    else:
        try:
            validate_password(request.POST["password"])
        except ValidationError as e:
            for i in e:
                errors.append(i)
        user = User.objects.create_user(username=request.POST["name"], email=request.POST["email"], password=request.POST["password"])

    return render(request, "authenticate/login.html", {"errors": errors})
