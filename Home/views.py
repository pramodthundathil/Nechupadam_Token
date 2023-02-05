from django.shortcuts import render,redirect
from .forms import PatientAddForm,TreatmentCategoryForm,ChairNumberForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .decorators import Admin_only
from django.contrib.auth.decorators import login_required
from .models import PatientList,TreatmentCategory,ChairNumber,TokenGenerator

def SignIn(request):
    if request.method == "POST":
        username = request.POST["uname"]
        password = request.POST["pswd"]
        user = authenticate(request,username= username,password = password)
        if user is not None:
            login(request,user)
            return redirect('Index')
        else:
            messages.info(request,"Username or Password Incorrect")
            return redirect('SignIn')
    return render(request,'login.html')

def SignOut(request):
    logout(request)
    return redirect('SignIn')

@login_required(login_url="SignIn")
@Admin_only
def Index(request):
    patients = TokenGenerator.objects.filter(status = False)
    form = PatientAddForm()
    context = {
        "form":form,
        "patients":patients
    }
    return render(request,"Index.html",context)

@login_required(login_url="SignIn")
def TableView(request):
    patients = TokenGenerator.objects.filter(status = False)
    return render(request,"table.html",{"patients":patients})

@login_required(login_url="SignIn")
def AddScreen(request):
    form = PatientAddForm()
    form1 = TreatmentCategoryForm()
    form2 = ChairNumberForm()
    tCat = TreatmentCategory.objects.all()
    chair = ChairNumber.objects.all()
    
    context = {
        "form":form,
        "form1":form1,
        "form2":form2,
        "tcat":tCat,
        "chair":chair,
    }
    return render(request,"categoryadd.html",context)

@login_required(login_url="SignIn")
def AddCategory(request):
    if request.method == "POST":
        form = TreatmentCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,"New Category Added")
        else:
            messages.info(request,"Action Not Succeeded")
    return redirect('AddScreen')

@login_required(login_url="SignIn")
def AddChair(request):
    if request.method == "POST":
        form = ChairNumberForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,"New Chair Added")
        else:
            messages.info(request,"Action Not Succeeded")
    return redirect('AddScreen')

@login_required(login_url="SignIn")
def DeleteCategory(request,pk):
    item = TreatmentCategory.objects.get(id = pk)
    item.delete()
    messages.info(request,"Item deleted")
    return redirect('AddScreen')

@login_required(login_url="SignIn")
def DeleteChair(request,pk):
    chair = ChairNumber.objects.get(id =pk)
    chair.delete()
    messages.info(request,"Chair deleted")
    return redirect('AddScreen')

@login_required(login_url="SignIn")
def AddPatient(request):
    if request.method == "POST":
        form = PatientAddForm(request.POST)
        if form.is_valid():
            patient = form.save()
            patient.save()
            try:
                token = TokenGenerator.objects.all().last()
                tkn = token.token
                newtkn = int(tkn)+1
                gentkn = TokenGenerator.objects.create(Patient = patient,token = newtkn)
                gentkn.save()
            except:
                newtkn = 1
                gentkn = TokenGenerator.objects.create(Patient = patient,token = newtkn)
                gentkn.save()
                
            messages.info(request,"Patient Appoinment Added Successfully")
        else:
            messages.info(request,"Action Not Succeeded")
    return redirect('Index')

@login_required(login_url="SignIn")
def StatusChange(request,pk):
    token = TokenGenerator.objects.get(id = pk)
    token.status = True
    token.call_status = "served"
    token.save()
    token.Patient.Status = True
    token.Patient.save()
    messages.info(request,"Item Changed")
    return redirect('Index')

@login_required(login_url="SignIn")
def History(request):
    form = PatientAddForm()
    patients = PatientList.objects.all().order_by("Status")
    context = {
        "patients":patients,
        "form":form
    }
    return render(request,"history.html",context)

@login_required(login_url="SignIn")
def TokenCall(request,pk):
    token = TokenGenerator.objects.get(id = pk)
    if token.call_status == "serving":
        token.call_status = None
    else:
        token.call_status = "serving"
    token.save()
    return redirect('Index') 

@login_required(login_url="SignIn")
def TokenReset(request):
    token = TokenGenerator.objects.all()
    token.delete()
    patients = PatientList.objects.all()
    for i in patients:
        i.Status = True
        i.save()
    messages.info(request,"All Tokens Cleared")
    return redirect("AddScreen")

def DeletePatient(request,pk):
    patient = PatientList.objects.get(id = pk)
    patient.delete()
    messages.info(request,"Patient History Deleted")
    return redirect('History')

def ClearHistory(request):
    patients = PatientList.objects.all().filter(Status=True)
    patients.delete()
    messages.info(request,"All History Deleted")
    return redirect("AddScreen")
    