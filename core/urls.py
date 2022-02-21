
from django.urls import path

from .views import Home,Contest_data,Contestcategory_edit,Create_Contest,Createcontestcategory_edit,Sponcer_Home,Sponsor_edit,Contest_Prize,Contest_Prize_Edit,User_logout,PYF_Users_Home,PYF_Users_Edit
urlpatterns = [
   
    path('',Home.as_view(),name="index"),
    path('contest_home', Contest_data.as_view(), name='contest_home'),
    path('edit_contest_category/<int:id>/',Contestcategory_edit.as_view(),name="edit_contest_category"),
    path('create_contest_category', Create_Contest.as_view(), name='create_contest_category'),
    path('edit_create_contest_category/<int:id>/',Createcontestcategory_edit.as_view(),name="edit_create_contest_category"),
    path('sponcer', Sponcer_Home.as_view(), name='sponcer'),
    path('editsponcer/<int:id>/',Sponsor_edit.as_view(),name="editsponcer"),
    path('contest_prize_home', Contest_Prize.as_view(), name='contest_prize_home'),
    path('contest_prize_edit/<int:id>/',Contest_Prize_Edit.as_view(),name="contest_prize_edit"),
    path('pyf_user', PYF_Users_Home.as_view(), name='pyf_user'),
    path('pyfuser_edit/<int:id>/', PYF_Users_Edit.as_view(), name='pyfuser_edit'),
    path('logout', User_logout.as_view(), name='logout'),
]