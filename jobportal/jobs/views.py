from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    return render(request,'index.html')
def admin_login(request):
    error = ""

    if request.method == "POST":
        u = request.POST.get('username')
        p = request.POST.get('password')

        user = authenticate(username=u, password=p)

        if user and user.is_superuser:
            login(request, user)
            return redirect('/admin/')
        else:
            error = "Invalid admin credentials"

    return render(request, 'admin_login.html', {'error': error})
def recruiter_login(request):
    error = ""

    if request.method == "POST":
        u = request.POST.get('username')
        p = request.POST.get('password')

        user = authenticate(username=u, password=p)

        if user:
            login(request, user)

            try:
                data = Studentuser.objects.get(user=user)

                if data.type == "recruiter":
                    return redirect('recruiter_dashboard')
                else:
                    logout(request)
                    error = "You are not a recruiter"

            except:
                logout(request)
                error = "Profile not found"

        else:
            error = "Invalid username or password"

    return render(request, 'recruiter_login.html', {'error': error})

def recruiter_register(request):
    error = ""

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        mobile = request.POST.get('mobile')
        gender = request.POST.get('gender')
        image = request.FILES.get('image')

        try:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )

            Studentuser.objects.create(
                user=user,
                mobile=mobile,
                gender=gender,
                image=image,
                type="recruiter"
            )

            error = "no"

        except:
            error = "yes"

    return render(request, 'recruiter_register.html', {'error': error})

# ================= LOGIN =================
def user_login(request):
    error = False

    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')

        user = authenticate(username=u, password=p)

        if user:
            login(request, user)
            return redirect('job_list')
        else:
            error = True

    return render(request, 'user.html', {'error': error})
# ================= LOGOUT =================
def user_logout(request):
    logout(request)
    return redirect('user_login')


# ================= JOB LIST =================
def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'job_list.html', {'jobs': jobs})


# ================= SEARCH JOB =================
def search_job(request):
    query = request.GET.get('q')
    jobs = Job.objects.filter(title__icontains=query)
    return render(request, 'job_list.html', {'jobs': jobs})


# ================= APPLY JOB =================
def apply_job(request, id):
    job = get_object_or_404(Job, id=id)

    if not Application.objects.filter(user=request.user, job=job).exists():
        Application.objects.create(user=request.user, job=job)

    return redirect('my_applications')


# ================= MY APPLICATIONS =================
def my_applications(request):
    apps = Application.objects.filter(user=request.user)
    return render(request, 'applications.html', {'apps': apps})


# ================= DELETE APPLICATION =================
def delete_application(request, id):
    app = get_object_or_404(Application, id=id, user=request.user)
    app.delete()
    return redirect('my_applications')


def register(request):
    error = ""

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        mobile = request.POST.get('mobile')
        gender = request.POST.get('gender')
        image = request.FILES.get('image')

        try:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )

            Studentuser.objects.create(
                user=user,
                mobile=mobile,
                gender=gender,
                image=image,
                type="user"   # default role
            )

            error = "no"

        except Exception as e:
            print(e)   
            error = "yes"

    return render(request, 'register.html', {'error': error})

from django.contrib.auth.decorators import login_required


@login_required
def add_job(request):

    data = Studentuser.objects.get(user=request.user)

    if data.type != "recruiter":
        return redirect('index')

    if request.method == 'POST':
        Job.objects.create(
            recruiter=request.user,
            title=request.POST.get('title'),
            company=request.POST.get('company'),
            location=request.POST.get('location'),
            description=request.POST.get('description')
        )
        return redirect('recruiter_dashboard')

    return render(request, 'add_job.html')


from django.contrib.auth.decorators import login_required

@login_required
def recruiter_dashboard(request):
    jobs = Job.objects.filter(recruiter=request.user)
    return render(request, 'recruiter_dashboard.html', {'jobs': jobs})

def applicant_detail(request, id):
    app = get_object_or_404(Application, id=id)
    return render(request, 'applicant_detail.html', {'app': app})