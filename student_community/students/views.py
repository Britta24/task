from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import StudentProfile
from internships.models import Internship
from applications.models import Application



def home(request):
    return render(request, "index.html")


@login_required
def student_dashboard(request):

   
    profile, created = StudentProfile.objects.get_or_create(user=request.user)

  
    if request.method == "POST" and "save_profile" in request.POST:

        profile.name = request.POST.get("name")
        profile.college = request.POST.get("college")
        profile.course = request.POST.get("course")
        profile.contact = request.POST.get("contact")
        profile.skills = request.POST.get("skills")

        if request.FILES.get("resume"):
            profile.resume = request.FILES.get("resume")

        profile.save()
        return redirect("student_dashboard")


   
    internships = Internship.objects.select_related(
    "company",
    "company__user"
).all().order_by("-id")

    applications = Application.objects.filter(
        student=profile
    ).select_related("internship", "internship__company")

    applied_ids = applications.values_list("internship_id", flat=True)


    context = {
        "profile": profile,
        "internships": internships,
        "applications": applications,
        "applied_ids": applied_ids,   
    }

    return render(request, "student.html", context)



@login_required
def apply_internship(request, pk):

    if request.method == "POST":

        profile, created = StudentProfile.objects.get_or_create(user=request.user)

       
        if not profile.name:
            return redirect("student_dashboard")

        internship = get_object_or_404(Internship, id=pk)

        Application.objects.get_or_create(
            student=profile,
            internship=internship,
            defaults={"status": "Applied"}
        )

    return redirect("student_dashboard")