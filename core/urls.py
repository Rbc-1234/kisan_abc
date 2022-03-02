from core import views
from django.urls import path


from .views import Home,Contest_data,Contestcategory_edit,Create_Contest,Createcontestcategory_edit,Sponcer_Home,Sponsor_edit,Contest_Prize,Contest_Prize_Edit,User_logout,PYF_Users_Home,PYF_Users_Edit,form,Blog_home,Blog_Edit,Reachus_home,Reachus_home_form
urlpatterns = [
   
    path('',Home.as_view(),name="index"),
    path('view-category', Contest_data.as_view(), name='view-category'),
    path('create-contest-category/<int:id>/',Contestcategory_edit.as_view(),name="create-contest-category"),
    path('view-contest', Create_Contest.as_view(), name='view-contest'),
    path('create-contest/<int:id>/',Createcontestcategory_edit.as_view(),name="create-contest"),
    path('view-sponcer', Sponcer_Home.as_view(), name='view-sponcer'),
    path('create-contest-sponsor/<int:id>/',Sponsor_edit.as_view(),name="create-contest-sponsor"),
    path('view-contest-prize', Contest_Prize.as_view(), name='view-contest-prize'),
    path('create-contest-prize/<int:id>/',Contest_Prize_Edit.as_view(),name="create-contest-prize"),
    path('users', PYF_Users_Home.as_view(), name='users'),
    path('pyfuser_edit/<int:id>/', PYF_Users_Edit.as_view(), name='pyfuser_edit'),
    path('logout', User_logout.as_view(), name='logout'),
    path('pyf_user', views.form, name='pyf_user'),
    path('statusChangeUser', views.statusChangeUser, name='statusChangeUser'),
    path('statusChangeUsers', views.statusChangeUsers, name='statusChangeUsers'),
    path('bloghome', Blog_home.as_view(), name='bloghome'),
    path('blogedit/<int:id>/', Blog_Edit.as_view(), name='blogedit'),
    path('view-reach-Enquiries', Reachus_home.as_view(), name='view-reach-Enquiries'),
    path('reachusform/<int:id>/', Reachus_home_form.as_view(), name='reachusform'),
    
]