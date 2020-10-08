from django.urls import path
from django.contrib.auth import views as auth_views


from . import views

app_name = "core"

urlpatterns = [
    path(r'dashboard/', views.HomeView.as_view(), name='home'),
    path(r'dashboard/employee/create', views.EmployeeCreateView.as_view(), name='employee_create'),
    path(r'dashboard/employee_department/create/<int:pk>', views.EmployeeDepartmentCreateView.as_view(), name='employee_department_create'),
    path(r'dashboard/employee_department/change/<int:pk>', views.EmployeeDepartmentChangeCreateView.as_view(), name='employee_department_change'),
    path(r'dashboard/employee_leave/add/<int:pk>', views.EmployeeLeaveCreateView.as_view(), name='employee_leave_add'),
    path(r'dashboard/employee_position/create/<int:pk>', views.EmployeePositionCreateView.as_view(), name='employee_position_create'),
    path(r'dashboard/employee_position/change/<int:pk>', views.EmployeePositionChangeCreateView.as_view(), name='employee_position_change'),
    path(r'dashboard/employee/list', views.EmployeeListView.as_view(), name='employee_list'),
    path(r'dashboard/employee/update/<int:pk>', views.EmployeeUpdateView.as_view(), name='employee_update'),
    path(r'dashboard/employee/detail/<int:pk>', views.EmployeeDetailView.as_view(), name='employee_detail'),
    path(r'dashboard/employee/delete/<int:pk>', views.EmployeeDeleteView.as_view(), name='employee_delete'),
    path(r'dashboard/postion/create', views.PositionCreateView.as_view(), name='position_create'),
    path(r'dashboard/position/list', views.PositionListView.as_view(), name='position_list'),
    path(r'dashboard/position/update/<int:pk>', views.PositionUpdateView.as_view(), name='position_update'),
    path(r'dashboard/position/delete/<int:pk>', views.PositionDeleteView.as_view(), name='position_delete'),
    path(r'dashboard/leave/create', views.LeaveCreateView.as_view(), name='leave_create'),
    path(r'dashboard/leave/list', views.LeaveListView.as_view(), name='leave_list'),
    path(r'dashboard/leave/update/<int:pk>', views.LeaveUpdateView.as_view(), name='leave_update'),
    path(r'dashboard/leave/delete/<int:pk>', views.LeaveDeleteView.as_view(), name='leave_delete'),
    path(r'dashboard/department/create', views.DepartmentCreateView.as_view(), name='department_create'),
    path(r'dashboard/department/list', views.DepartmentListView.as_view(), name='department_list'),
    path(r'dashboard/department/update/<int:pk>', views.DepartmentUpdateView.as_view(), name='department_update'),
    path(r'dashboard/department/delete/<int:pk>', views.DepartmentDeleteView.as_view(), name='department_delete'),
    path(r'accounts/login', auth_views.LoginView.as_view(), name='login'),
    path(r'accounts/logout', auth_views.LogoutView.as_view(), name='logout'),
]