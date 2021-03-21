
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    #path('<name>/<age>',info),
    path('add-district',add_district),
    path('district-detail/<name>',dist_detail, name="dist_detail"),
    path('all-division',all_division,name="all-division"),
    path('all-district',all_district,name="all-district"),
    path('div-wise-district/<name>',div_wise_district,name="div_wise_district"),
    path('user-form', user_forms, name="user_form")
]
