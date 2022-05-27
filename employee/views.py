from django.shortcuts import render,redirect
from employee.forms import EmpForm
from django.views.generic import View
from employee.models import Employee


# Create your views here.

class EmployeeCreateView(View):
    template_name="regform.html"
    def get(self,request,*args,**kwargs):
        form=EmpForm()
        return render(request,self.template_name,{"form":form})
    def post(self,request,*args,**kwargs):
        form=EmpForm(request.POST)
        # if form.is_valid():
        #     print(form.cleaned_data)
        #     return render(request,"regform.html",{"forms":form})
        # else:
        #     return render(request, "regform.html", {"forms": form})
        if not form.is_valid():
            return render(request, self.template_name, {"forms": form})
        form.save()
        return redirect("list-add")



class EmployeeListView(View):
    template_name="emp-list.html"

    def get(self,request,*args,**kwargs):
        qs=Employee.objects.all()
        return render(request,self.template_name,{"employee":qs})

class EmployeeDetailView(View):
    template_name="emp-details.html"
    def get_object(self,id):
        return Employee.objects.get(id=id)
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        emp=self.get_object(id)
        return render(request,self.template_name,{"employee":emp})


