"""PMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from . import doctor_ctrl
from .import patient_ctrl
from .import admin_ctrl
from .import dailyreport_ctrl
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('doctorinterface/', doctor_ctrl.doctor_interface),
    path('doctorsubmit',doctor_ctrl.doctor_submit),
    path('doctordisplayall/',doctor_ctrl.display_all),
    path('doctordisplaybyid/',doctor_ctrl.display_by_id),
    path('editdoctor/', doctor_ctrl.edit_doctor),
    path('editpicture', doctor_ctrl.edit_picture),path('patientinterface/', patient_ctrl.patient_interface),
    path('patientsubmit', patient_ctrl.patient_submit),
    path('patientdisplayall/', patient_ctrl.display_all),
    path('patientdisplaybyid/', patient_ctrl.display_by_id),
    path('editpatient/', patient_ctrl.edit_patient),
    path('editpicture', patient_ctrl.edit_picture),
    path('adminlogin/', admin_ctrl.admin_login),
    path('checkadminlogin', admin_ctrl.check_login),
    path('dailyreport/', dailyreport_ctrl.dailyreport_interface),
    path('dailyreportsubmit', dailyreport_ctrl.dailyreport_submit),
    path('doctorlogin/', doctor_ctrl.doctor_login),
    path('checkdoctorlogin', doctor_ctrl.check_login),
    path('searchpatient/', patient_ctrl.search_patient),
    path("home/",admin_ctrl.index),

]
urlpatterns+=staticfiles_urlpatterns()
