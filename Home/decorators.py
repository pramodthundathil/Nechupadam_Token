from django.shortcuts import redirect

def Admin_only(view_func):
    def wrapper_func(request,*args,**kwargs):
        group = None
        if request.user.groups.all().exists():
            group = request.user.groups.all()[0].name
        if group == None:
            return view_func(request,*args,**kwargs)
        if group == "tvviewer":
            return redirect("TableView")
    return wrapper_func

def unautenticated_user(view_func):
    def wrapper_func(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('Index')
        else:
            return view_func(request,*args,**kwargs)
        
    return wrapper_func