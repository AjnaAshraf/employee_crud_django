from django.shortcuts import render

from django.views.generic import View

from crm.models import Employee

from django.http import JsonResponse

from json import loads

from django.views.decorators.csrf import csrf_exempt

from django.utils.decorators import method_decorator
# Create your views here.

@method_decorator(csrf_exempt,name="dispatch")
class EmployeeCreateListView(View):

    def get(self,request):

        qs = Employee.objects.all().values()

        employee_list = list(qs)

        return JsonResponse(employee_list,safe=False)

    def post(self,request):

        form_data = loads(request.body)

        """
            "name":"Ajna",
            "department":"IT",
            "salary":56000,
            "location":"EKM",
            "email":"ajnaashraf@gmail.com"
                    
        """

        Employee.objects.create(
            name=form_data.get("name"),
            department = form_data.get("department"),
            salary = form_data.get("salary"),
            location = form_data.get("location"),
            email = form_data.get("email")

            )

        return JsonResponse({"message": "Record created ......"})
@method_decorator(csrf_exempt,name="dispatch")
class EmployeeRetrieveUpdateDeleteView(View):

    def get(self,request,pk = None):

        qs = Employee.objects.filter(id = pk).values()

        employee_detail = list(qs)

        return JsonResponse(employee_detail,safe=False)

    def delete(self,request,pk = None):

        qs = Employee.objects.get(id = pk).delete()

        return JsonResponse({"message":"Record deleted..."},)
