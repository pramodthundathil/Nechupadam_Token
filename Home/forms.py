from django.forms import ModelForm,TextInput
from .models import PatientList,ChairNumber,TreatmentCategory

class PatientAddForm(ModelForm):
    class Meta:
        model = PatientList
        fields = ["Patients_Name","Patients_Age","Phone_Number","Treatment_Category","Chair_Number",]
        
        widgets = {
            "Patients_Name":TextInput(attrs={"placeholder":"Patient Name"}),
            "Patients_Age":TextInput(attrs={"placeholder":"Patient Age"}),
            "Phone_Number":TextInput(attrs={"type":"number","placeholder":"Phone Number"}),    
            
        }
        
class ChairNumberForm(ModelForm):
    class Meta:
        model = ChairNumber
        fields = "__all__"
        widgets = {
            "Chair_number":TextInput(attrs={"placeholder":"Enetr Chair Number"})
        }
        
class TreatmentCategoryForm(ModelForm):
    class Meta:
        model = TreatmentCategory
        fields = "__all__"
        widgets = {
            "title":TextInput(attrs={"placeholder":"Enetr Category"})
        }