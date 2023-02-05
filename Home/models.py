from django.db import models



class TreatmentCategory(models.Model):
    title = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title
    
class ChairNumber(models.Model):
    Chair_number = models.CharField(max_length=255)
    
    def __str__(self):
        return self.Chair_number
    
class PatientList(models.Model):
    
    Patients_Name = models.CharField(max_length=255)
    Patients_Age = models.CharField(max_length=11,null=True)
    Phone_Number = models.IntegerField()
    Treatment_Category = models.ForeignKey(TreatmentCategory,on_delete=models.SET_NULL,null=True)
    Chair_Number = models.ForeignKey(ChairNumber,on_delete=models.SET_NULL,null=True)
    Date = models.DateTimeField(auto_now_add=True) 
    Status = models.BooleanField(default=False)
    
class TokenGenerator(models.Model):
    Patient = models.ForeignKey(PatientList,on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    token = models.CharField(max_length=11)
    call_status = models.CharField(max_length=255,null=True,blank=True)
    status = models.BooleanField(default=False)
