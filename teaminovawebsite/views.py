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
    success = False

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirmPassword")
        name = request.POST.get("name")

        current_user = User.objects.filter(email=email).first()

        if current_user:
            errors.append("The given email is already being used")
        elif password != confirm_password:
            errors.append("Passwords don't match")
        else:
            try:
                validate_password(password)
            except ValidationError as e:
                errors.extend(e)
            else:
                User.objects.create_user(username=name, email=email, password=password)
                success = True if not errors else False

    return render(request, "authenticate/login.html", {"errors": errors, "success": success})
