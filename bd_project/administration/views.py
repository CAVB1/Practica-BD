from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.views import generic
from django.utils import timezone
from django.urls import reverse

from .models import User, Table, Control, Privilege, Product

# Create your views here.


def index(request):
    return render(request, "administration/index.html",{})

def users(request):
    user_list= User.objects.order_by("-update_date")

    context = {
        "obj_list":user_list,
        "interface": "Usuarios"
    }

    return render(request, "administration/users.html", context)
def privileges(request):
    user_list= Privilege.objects.all()

    context = {
        "obj_list":user_list,
        "interface": "Privilegios"
    }

    return render(request, "administration/users.html", context)
def tables(request):
    user_list= Table.objects.all()

    context = {
        "obj_list":user_list,
        "interface": "Tablas"
    }

    return render(request, "administration/users.html", context)


def newUser(request):
    return render(request, "administration/new_user.html", {})

def saveUser(request):
    try:
        user = User(username=request.POST['username'], 
                    password=request.POST['password'],
                    name= request.POST['name'],
                    rol = request.POST['rol'],
                    update_date = timezone.now()
                    )
        user.save()
    except (Exception):
        return render(
            request,
            "administration/new_user.html",
            {
                "error_message": "Algo ha salido mal"
            }
        )
    else:
        return HttpResponseRedirect(reverse("administration:users"))
    
def newTable(request):
    return render(request, "administration/new_table.html", {})

def saveTable(request):
    try:
        table = Table(table=request.POST['table'], 
                    description=request.POST['description']
                    
                    )
        table.save()
    except (Exception):
        return render(
            request,
            "administration/new_table.html",
            {
                "error_message": "Algo ha salido mal"
            }
        )
    else:
        return HttpResponseRedirect(reverse("administration:tables"))
    


def newPrivilege(request):
    return render(request, "administration/new_priv.html", {})

def savePrivilege(request):
    try:
        priv = Privilege(privilege=request.POST['priv'], 
                    description=request.POST['description']
                    
                    )
        priv.save()
    except (Exception):
        return render(
            request,
            "administration/new_table.html",
            {
                "error_message": "Algo ha salido mal"
            }
        )
    else:
        return HttpResponseRedirect(reverse("administration:privileges"))
    
def deleteUser(request, user_id):
    user = get_object_or_404(User,pk=user_id)
    try:
        user.delete()
    except (KeyError, User.DoesNotExist):
        # Redisplay the question voting form.
        return HttpResponseRedirect(reverse("administration:users", args={}))
    else:
        return HttpResponseRedirect(reverse("administration:users", args={}))
    

def deleteTable(request, table_id):
    table = get_object_or_404(Table,pk=table_id)
    try:
        table.delete()
    except (KeyError, Table.DoesNotExist):
        # Redisplay the question voting form.
        return HttpResponseRedirect(reverse("administration:tables", args={}))
    else:
        return HttpResponseRedirect(reverse("administration:tables", args={}))
    
def deletePrivilege(request, priv_id):
    priv = get_object_or_404(Privilege,pk=priv_id)
    try:
        priv.delete()
    except (KeyError, Privilege.DoesNotExist):
        # Redisplay the question voting form.
        return HttpResponseRedirect(reverse("administration:privileges", args={}))
    else:
        return HttpResponseRedirect(reverse("administration:privileges", args={}))
    

def editUser(request, user_id):
    tables={}
    privileges ={}

    for t in Table.objects.all():
        tables[t.id] = t.table
    for p in Privilege.objects.all():
        privileges[p.id]=p.privilege

    user=get_object_or_404(User, pk=user_id)
    priv = user.control_set.all()
    privs = {}

    for p in priv:
        privs[Table.objects.get(pk=p.table.id).table]=Privilege.objects.get(pk=p.privilege.id).privilege

    return render(request, "administration/new_user.html", {"user_obj":user,"privs":priv, "privileges":privileges, "tables":tables})

def updateUser(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    try:
        user.username=request.POST['username']
        user.password=request.POST['password']
        user.name=request.POST['name']
        user.rol=request.POST['rol']
        user.update_date=timezone.now()

        user.save()
        
    except(KeyError, User.DoesNotExist):
        return render(
            request,
            "administration/new_user.html",
            {
                "error_message": "Algo ha salido mal",
                "user_obj": User.objects.get(pk=user_id),
            }
        )
    else:
        return HttpResponseRedirect(reverse("administration:users",args={}))
    

def addUserPrivilege(request, user_id, id_table, id_privilege):
    control = Control.objects.filter(user=user_id, table=id_table, privilege=id_privilege)

    if control:
        return HttpResponseRedirect(reverse("administration:edit_user",args={user_id}))
    else:
        c = Control(user=User.objects.get(pk=user_id) , table= Table.objects.get(pk=id_table) , privilege=Privilege.objects.get(pk=id_privilege))
        c.save()
        return HttpResponseRedirect(reverse("administration:edit_user",args={user_id}))
    

def Query(request):
    tables = Table.objects.all()
    table_list = []

    for t in tables:
        table_list.append([t.id,t.table])

    return render(request, "administration/querys.html",{"table_list":table_list})

def querySelect(request):
    user = User.objects.filter(username=request.POST['username']).filter(password=request.POST['password'])

    if user:
        if Control.objects.filter(user=user.id).filter(table=request.POST['table']).filter(privilege=request.POST['type']):
            if request.POST['type']==1 and request.POST['type-q']=="all":
                list=Product.objects.all().__dict__
                return HttpResponse({"value": list})


    else:
        return HttpResponse({"value":"Error de usuario o contraseña"})
        

    