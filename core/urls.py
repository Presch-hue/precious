
from pydoc import pager
from django.contrib import admin
from django.urls import path
from app.views import *
from app import views

urlpatterns = [
    path("", home, name=""),
    path('admin/', admin.site.urls),
    path('auth/signout/', LogoutView.as_view())
]

urlpatterns += [
    path('student/login/', StudentLoginView.as_view(), name='student_login'),
    path('student/profile/', StudentProfileView.as_view()),
    path('student/dashboard/', StudentDashboardView.as_view()),
    path('student/test-results/', StudentTestResultsView.as_view()),
    path('student/appointments/', StudentAppointmentView.as_view()),
    path('student/appointments/cancel/<appointment_id>/', StudentAppointmentCancelView.as_view()),
    path('student/appointments/delete/<appointment_id>/', StudentAppointmentDeleteView.as_view()),
    path('student/prescriptions/view/<appointment_id>/', StudentAppointmentPrescriptionView.as_view()),
    path('student/prescriptions/view/', StudentPrescriptionListView.as_view(), name ="student_prescriptions"),
    path('student/signup/', views.student_signup, name='student_signup'),
]

urlpatterns += [
    path('doctor/login/', DoctorLoginView.as_view(), name='doctor_login'),
    path('doctor/profile/', DoctorProfileView.as_view()),
    path('doctor/dashboard/', DoctorDashboardView.as_view()),
    path('doctor/appointments/', DoctorAppointmentView.as_view()),
    path('doctor/appointments/cancel/<appointment_id>/', DoctorAppointmentCancelView.as_view()),
    path('doctor/appointments/approve/<appointment_id>/', DoctorAppointmentApproveView.as_view()),
    path('doctor/appointments/prescribe/<appointment_id>/', DoctorPrescriptionView.as_view()),
    path('doctor/test-result/add/', DoctorStudentRecordAdditionView.as_view()),
    path('doctor/signup/', views.doctor_signup, name='doctor_signup'),
]

from django.conf import settings
from django.conf.urls.static import static

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)