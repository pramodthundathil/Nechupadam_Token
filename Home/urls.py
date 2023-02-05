from django.urls import path 
from .import views

urlpatterns = [
    path("",views.SignIn,name="SignIn"),
    path("Index",views.Index,name="Index"),
    path("TableView",views.TableView,name="TableView"),
    path("AddScreen",views.AddScreen,name="AddScreen"),
    path("SignOut",views.SignOut,name="SignOut"),
    path("AddCategory",views.AddCategory,name="AddCategory"),
    path("AddChair",views.AddChair,name="AddChair"),
    path("DeleteCategory/<int:pk>",views.DeleteCategory,name="DeleteCategory"),
    path("DeleteChair/<int:pk>",views.DeleteChair,name="DeleteChair"),
    path("AddPatient",views.AddPatient,name="AddPatient"),
    path("StatusChange/<int:pk>",views.StatusChange,name="StatusChange"),
    path("History",views.History,name="History"),
    path("TokenCall/<int:pk>",views.TokenCall,name="TokenCall"),
    path("TokenReset",views.TokenReset,name="TokenReset"),
    path("DeletePatient/<int:pk>",views.DeletePatient,name="DeletePatient"),
    path("ClearHistory",views.ClearHistory,name="ClearHistory")
]
