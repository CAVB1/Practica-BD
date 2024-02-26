from django.urls import path
from . import views

app_name="administration"
urlpatterns=[
    path("",views.index, name="index"),
    path("/Users/", views.users, name="users"),
    path("/Users/New", views.newUser, name="new_user"),
    path("/Users/SaveUser", views.saveUser, name="save_user"),
    path("/Users/<int:user_id>/Delete",views.deleteUser,name="delete_user"),
    path("/Users/<int:user_id>/EditUser",views.editUser,name="edit_user"),
    path("/Users/<int:user_id>/UpdateUser",views.updateUser,name="update_user"),
    path("/Users/<int:user_id>/addPrivilege/<int:id_table>/<int:id_privilege>/",views.addUserPrivilege,name="add_user_privilege"),
    path("/Privileges/", views.privileges, name="privileges"),
    path("/Privileges/New", views.newPrivilege, name="new_privilege"),
    path("/Privileges/SavePrivilege", views.savePrivilege, name="save_privilege"),
    path("/Privileges/<int:priv_id>/Delete",views.deletePrivilege ,name="delete_privilege"),
    path("/Privileges/<int:privilege_id>/EditPrivilege", views.editPrivilege, name="edit_privilege"),
    path("/Privileges/<int:privilege_id>/UpdatePrivilege", views.updatePrivilege, name="update_privilege"),
    path("/Tables/", views.tables, name="tables"),
    path("/Tables/New", views.newTable, name="new_table"),
    path("/Tables/SaveTable", views.saveTable, name="save_table"),
    path("/Tables/<int:table_id>/Delete",views.deleteTable,name="delete_table"),
    path("/Tables/<int:table_id>/EditTable",views.editTable,name="edit_table"),
    path("/Tables/<int:table_id>/UpdateTable",views.updateTable,name="update_table"),

    path("/Querys/", views.Query, name="query"),
    path("/Querys/Select", views.querySelect, name="query_select"),
    
]