from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

User = get_user_model()


def register(request):
    role = request.GET.get("role")

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

       
        if role not in ["student", "company"]:
            return redirect("home")

        if User.objects.filter(username=email).exists():
            return render(request, "register.html", {
                "role": role,
                "error": "Email already registered"
            })

       
        User.objects.create_user(
            username=email,
            email=email,
            password=password,
            user_type=role
        )

        return redirect(f"/login/?role={role}")

    return render(request, "register.html", {"role": role})



def user_login(request):
    role = request.GET.get("role")

    if request.method == "POST":

        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=email,
            password=password
        )

        if user is not None:

            if role and user.user_type != role:
                return render(request, "login.html", {
                    "role": role,
                    "error": "You are registered as a different role"
                })

            login(request, user)
            return redirect("dashboard")

        return render(request, "login.html", {
            "role": role,
            "error": "Invalid email or password"
        })

    return render(request, "login.html", {"role": role})


@login_required
def user_logout(request):
    logout(request)
    return redirect("home")



@login_required
def dashboard_redirect(request):

    if request.user.user_type == "student":
        return redirect("student_dashboard")

    if request.user.user_type == "company":
        return redirect("company_dashboard")

    return redirect("login")