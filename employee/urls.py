from django.urls import path,include
from employee import views


urlpatterns=[
    path("add",views.EmployeeCreateView.as_view(),name="emp-add"),
    path("all",views.EmployeeListView.as_view(),name="list-emp"),
    path("details/<int:id>",views.EmployeeDetailView.as_view(),name="detail"),


]