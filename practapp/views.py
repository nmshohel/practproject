from django.shortcuts import render, HttpResponse
from .forms import *
from .models import *

# Create your views here.
from practapp.models import Division, Discrict


def home(request):
    return HttpResponse("This is home page")


def info(request, name, age):
    result = "my name is " + name + " and age is " + age
    return HttpResponse(result)


def all_division(request):
    divisions = Division.objects.all()
    context = {'divisions': divisions}
    return render(request, 'all_division.html', context)


def all_district(request):
    discricts = Discrict.objects.all()
    context = {'discricts': discricts}
    return render(request, 'all_district.html', context)

def div_wise_district(request, name):
    districts=Discrict.objects.filter(division__name= name)
    print(districts)
    context={'districts':districts,'name':name}
    return render(request,'div_wise_dis.html',context)

def dist_detail(request,name):
    district = Discrict.objects.get(name= name)
    context={'district':district}
    return render(request,'dist_detail.html',context)

def add_district(request):
    form=DistrictForm()
    context={'form':form}
    return render(request,'add_district.html',context)

def user_forms(request):
    new_form=forms.user_form()
    context={'test_form':new_form,'heading_1':'This form create by libray'}

    if request.method=='POST':
        new_form=forms.user_form(request.POST)
        context.update({'test_form':new_form})
        if new_form.is_valid():
            user_name=new_form.cleaned_data['user_name']
            dob=new_form.cleaned_data['user_dob']
            user_eamil=new_form.cleaned_data['user_email']
            user_attendence=new_form.cleaned_data['attendence']
            department=new_form.cleaned_data['department']
            context.update({'user_name':user_name})
            context.update({'dob':dob})
            context.update({'user_eamil':user_eamil})
            context.update({'user_attendence':user_attendence})
            context.update({'department':department})
            context.update({'form_submited':'Yes'})
    # new_form=forms.MusicianForm()
    # if request.method=='POST':
    #     new_form=forms.MusicianForm(request.POST)
    #     if new_form.is_valid():
    #         new_form.save(commit=True)
    # context={'test_form':new_form}

    return render(request,'user_form.html',context)

