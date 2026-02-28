"""
URL configuration for student_community project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from accounts.views import register, user_login, user_logout, dashboard_redirect
from students.views import home, student_dashboard, apply_internship
from companies.views import company_dashboard

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", home, name="home"),

    path("register/", register, name="register"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),

    path("dashboard/", dashboard_redirect, name="dashboard"),

    path("student/", student_dashboard, name="student_dashboard"),
    path("company/", company_dashboard, name="company_dashboard"),

    path("apply/<int:pk>/", apply_internship, name="apply_internship"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)