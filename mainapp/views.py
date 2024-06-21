from django.shortcuts import render , HttpResponse
from . import models
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import redirect
import hashlib
import random
# Create your views here.

def main_page(request):
    return render(request,"index.html")

def dash(request):
    return render(request,"main_page.html")

def deletedata(request,task_id):

    token = request.COOKIES.get("token")
    task_list = models.task_data.objects.get(task_create_by=token,task_id=task_id)
    task_list.status = "delete"
    task_list.save()
    return redirect("/dashboard")


def updatedata(request,task_id):
    
    task_list = models.task_data.objects.get(task_id=task_id)
    js_data = {
        "task_id":task_id,
        "title":task_list.title,
        "desc":task_list.desc,
        "due_date":task_list.due_date,
        "task_status":task_list.task_status    
    }
    print(js_data)
    return render(request,"update.html",js_data)


class hello(APIView):
    def get(self, request):
        return Response({"Mess":"Hello world"})
class userlogin(APIView):
    def get(self, request):
        return Response({"status":"Invalid Requests Method"})
    
    def post(self,request):
        email = request.data["email"]
        passwd = request.data["passwd"]

        check_found = models.user_data_app.objects.filter(email=email,password=passwd).exists()
        
        if check_found:
            data = models.user_data_app.objects.get(email=email,password=passwd)
            res =  Response({"status":"Success"})
            res.set_cookie(
                key='token',
                value=data.tokenval,
                max_age=3600

            )
            return res
        else:
            return Response({"status":"Invalid User Id or Password"})



class UserRegistrationView(APIView):
    def get(self, request):
        return Response({"status":"Invalid Requests"})
    def post(self, request):
       
       name = request.data["name"]
       email = request.data["email"]
       passwd = request.data["passwd"]

       check_email_found = models.user_data_app.objects.filter(email=email).exists()
       if check_email_found:
           return Response({"status":"Already Present User ID Please Login"})
       else:
           data_base = models.user_data_app()
           data_base.name = name
           data_base.email = email
           data_base.password = passwd
           email_bytes = email.encode('utf-8')
           email_hash = hashlib.sha256(email_bytes).hexdigest()
           data_base.tokenval = email_hash
           data_base.save()
           return Response({
               "status":"Success Register Please Login..."
           })
       

class addtask(APIView):
    def get(self,request):
        return Response({"status":"Invalid Method"})
    def post(self,request):
        title = request.data["title"]
        desc = request.data["desc"]
        due_date = request.data["due_date"]
        task_status = request.data["task_status"]

        task_create_by = request.COOKIES.get("token")
        random_number = random.randint(1, 1000)
        full_task = title + desc + str(random_number) + due_date + task_status + task_create_by

        task_bytes = full_task.encode('utf-8')
        task_hash = hashlib.sha256(task_bytes).hexdigest()

        task_id = task_hash

        data_base = models.task_data()

        data_base.title = title
        data_base.desc = desc
        data_base.due_date = due_date
        data_base.task_status = task_status
        data_base.task_create_by = task_create_by
        data_base.task_id = task_id
        data_base.status = "ok"
        data_base.save()

        return Response({
            "status":"Success",
            "task_id":task_id
        })



class addassignto(APIView):
    def get(self, request):
        return Response({"status":"Invalid Method"})
    
    def post(self,request):
        task_id = request.data["task_id"]
        assign_email = request.data["assign_email"]

        data_base = models.assing_task()

        data_base.task_id = task_id
        data_base.assign_email = assign_email
        data_base.status = "ok"

        data_base.save()

        return Response({
            "status":"Assign Sucessfully"
        })


class getemaillist(APIView):
    def get(self, request):
        email_list = models.user_data_app.objects.values_list('email',flat=True)
        return Response(email_list)



class gettasklist(APIView):
    def get(self, request):
        token = request.COOKIES.get("token")
        task_list = models.task_data.objects.filter(task_create_by=token,status="ok").values()
        return Response(task_list)


class getassignlist(APIView):
    def get(self, request):
        task_id = request.query_params.get('task_id')
        task_list = models.assing_task.objects.filter(task_id=task_id).values()
        return Response(task_list)
    


class gettodolist(APIView):
    def get(self, request):
        token = request.COOKIES.get("token")
        task_list = models.task_data.objects.filter(task_create_by=token,task_status="todo",status="ok").values()
        return Response(task_list)

class getinprolist(APIView):
    def get(self, request):
        token = request.COOKIES.get("token")
        task_list = models.task_data.objects.filter(task_create_by=token,task_status="inprogress",status="ok").values()
        return Response(task_list)

class getdonelist(APIView):
    def get(self, request):
        token = request.COOKIES.get("token")
        task_list = models.task_data.objects.filter(task_create_by=token,task_status="done",status="ok").values()
        return Response(task_list)

class deletetask(APIView):
    def post(self,request):
        token = request.COOKIES.get("token")
        task_id = request.data["task_id"]
        task_list = models.task_data.objects.get(task_create_by=token,task_id=task_id)
        task_list.status = "delete"
        task_list.save()
        return Response({"status":"Task is Delete"})