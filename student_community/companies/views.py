from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import CompanyProfile
from internships.models import Internship
from applications.models import Application


@login_required
def company_dashboard(request):

    profile, created = CompanyProfile.objects.get_or_create(user=request.user)

  
    if request.method == "POST" and "save_profile" in request.POST:

        profile.name = request.POST.get("name")
        profile.industry = request.POST.get("industry")
        profile.location = request.POST.get("location")
        profile.contact = request.POST.get("contact")
        profile.about = request.POST.get("about")
        profile.save()

        return redirect("company_dashboard")

    if request.method == "POST" and "post_internship" in request.POST:

        title = request.POST.get("title")
        deadline = request.POST.get("deadline")

        if title and deadline:
            Internship.objects.create(
                company=profile,
                title=title,
                deadline=deadline
            )

        return redirect("company_dashboard")

   
    if request.method == "POST" and "update_status" in request.POST:

        app_id = request.POST.get("app_id")
        status = request.POST.get("status")

        application = get_object_or_404(
            Application,
            id=app_id,
            internship__company=profile
        )

        application.status = status
        application.save()

        return redirect("company_dashboard")

    
    applications = Application.objects.filter(
        internship__company=profile
    ).select_related(
        "student",
        "internship",
        "internship__company"
    ).order_by("-id")

    context = {
        "profile": profile,
        "applications": applications,
    }

    return render(request, "company.html", context)