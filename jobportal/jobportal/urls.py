from django.contrib import admin
from django.urls import path
from jobs.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # Home
    path('', index, name="index"),

    # Auth
    path('register/', register, name="register"),
    path('user_login/', user_login, name='user_login'),
    path('logout/', user_logout, name='logout'),


    path('jobs/', job_list, name='job_list'),
    path('search/', search_job, name='search_job'),
    path('apply/<int:id>/', apply_job, name='apply_job'),
    path('applications/', my_applications, name='my_applications'),
    path('delete/<int:id>/', delete_application, name='delete_application'),
    path('applicant/<int:id>/', applicant_detail, name='applicant_detail'),
    # Optional (you already had)
    path('recruiter_dashboard/', recruiter_dashboard, name='recruiter_dashboard'),
    path('add_job/', add_job, name='add_job'),
    path('admin_login/', admin_login, name='admin_login'),
    path('recruiter_login/', recruiter_login, name='recruiter_login'),
    path('recruiter_register/', recruiter_register, name='recruiter_register'),
]

# Media files
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)