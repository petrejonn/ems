from datetime import date
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404
from django.views.generic import (ListView, CreateView,DeleteView,DetailView, UpdateView,)

from .models import Employee, Department, Leave, Position, EmployeeDepartment, EmployeePosition
from .forms import EmployeeCreateForm, EmployeeDepartmentCreateForm, EmployeePositionCreateForm, EmployeeLeaveCreateForm

class HomeView(ListView):
    model = Employee
    template_name = 'dashboard/index.html'

class EmployeeCreateView(CreateView):
    form_class = EmployeeCreateForm
    template_name = 'dashboard/employee/create.html'

    def get_success_url(self):
        return reverse("core:employee_department_create", kwargs={"pk": self.object.id})

class EmployeeDepartmentCreateView(CreateView):
    form_class = EmployeeDepartmentCreateForm
    template_name = 'dashboard/employee/department/create.html'

    def get_success_url(self):
        return reverse("core:employee_position_create", kwargs={"pk": self.object.employee.id})

    def get_initial(self):
        employee = get_object_or_404(Employee, id=self.kwargs.get("pk"))
        return {"employee": employee}

class EmployeeDepartmentChangeCreateView(CreateView):
    form_class = EmployeeDepartmentCreateForm
    template_name = 'dashboard/employee/department/change.html'

    def get_success_url(self):
        return reverse("core:employee_detail", kwargs={"pk": self.object.employee.id})

    def get_initial(self):
        employee = get_object_or_404(Employee, id=self.kwargs.get("pk"))
        old_dept = EmployeeDepartment.objects.filter(employee=employee, date_left=None)
        if(old_dept):
            old_dept = old_dept.get()
            old_dept.date_left = date.today()
            old_dept.save()
        return {"employee": employee}

class EmployeePositionCreateView(CreateView):
    form_class = EmployeePositionCreateForm
    template_name = 'dashboard/employee/position/create.html'

    def get_success_url(self):
        return reverse("core:employee_list")

    def get_initial(self):
        employee = get_object_or_404(Employee, id=self.kwargs.get("pk"))
        return {"employee": employee}

class EmployeePositionChangeCreateView(CreateView):
    form_class = EmployeePositionCreateForm
    template_name = 'dashboard/employee/position/change.html'

    def get_success_url(self):
        return reverse("core:employee_detail", kwargs={"pk": self.object.employee.id})

    def get_initial(self):
        employee = get_object_or_404(Employee, id=self.kwargs.get("pk"))
        old_pos = EmployeePosition.objects.filter(employee=employee, end_date=None)
        if(old_pos):
            old_pos = old_pos.get()
            old_pos.end_date = date.today()
            old_pos.save()
        return {"employee": employee}

class EmployeeLeaveCreateView(CreateView):
    form_class = EmployeeLeaveCreateForm
    template_name = 'dashboard/employee/leave/create.html'

    def get_success_url(self):
        return reverse("core:employee_detail", kwargs={"pk": self.object.employee.id})

    def get_initial(self):
        employee = get_object_or_404(Employee, id=self.kwargs.get("pk"))
        old_leave = EmployeePosition.objects.filter(employee=employee, end_date=None)
        if(old_leave):
            old_leave = old_leave.get()
            old_leave.end_date = date.today()
            old_leave.save()
        return {"employee": employee}

class EmployeeUpdateView(UpdateView):
    model = Employee
    template_name = 'dashboard/employee/update.html'
    success_url = reverse_lazy('core:employee_list')
    fields = ('first_name','last_name','other_name','date_of_birth','state_of_origin','lga_of_origin','employment_date','retirement_date','photograph','email','phone',)

class EmployeeListView(ListView):
    model = Employee
    template_name = 'dashboard/employee/list.html'


class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'dashboard/employee/detail.html'


class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'dashboard/employee/delete.html'
    success_url = reverse_lazy('core:employee_list')


class DepartmentCreateView(CreateView):
    model = Department
    template_name = 'dashboard/department/create.html'
    success_url = reverse_lazy('core:department_list')
    fields = ('title','description')

class DepartmentUpdateView(UpdateView):
    model = Department
    template_name = 'dashboard/department/update.html'
    success_url = reverse_lazy('core:department_list')
    fields = ('title','description')
class DepartmentListView(ListView):
    model = Department
    template_name = 'dashboard/department/list.html'

class DepartmentDeleteView(DeleteView):
    model = Department
    template_name = 'dashboard/department/delete.html'
    success_url = reverse_lazy('core:department_list')

class PositionCreateView(CreateView):
    model = Position
    template_name = 'dashboard/position/create.html'
    success_url = reverse_lazy('core:position_list')
    fields = ('title','description')

class PositionUpdateView(UpdateView):
    model = Position
    template_name = 'dashboard/position/update.html'
    success_url = reverse_lazy('core:position_list')
    fields = ('title','description')

class PositionListView(ListView):
    model = Position
    template_name = 'dashboard/position/list.html'

class PositionDeleteView(DeleteView):
    model = Position
    template_name = 'dashboard/position/delete.html'
    success_url = reverse_lazy('core:position_list')

class LeaveCreateView(CreateView):
    model = Leave
    template_name = 'dashboard/leave/create.html'
    success_url = reverse_lazy('core:leave_list')
    fields = ('title','description')

class LeaveUpdateView(UpdateView):
    model = Leave
    template_name = 'dashboard/leave/update.html'
    success_url = reverse_lazy('core:leave_list')
    fields = ('title','description')

class LeaveListView(ListView):
    model = Leave
    template_name = 'dashboard/leave/list.html'

class LeaveDeleteView(DeleteView):
    model = Leave
    template_name = 'dashboard/leave/delete.html'
    success_url = reverse_lazy('core:leave_list')


