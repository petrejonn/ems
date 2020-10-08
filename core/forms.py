from django import forms


from .models import Employee, EmployeeDepartment, EmployeePosition, EmployeeLeave



class EmployeeCreateForm(forms.ModelForm):
    date_of_birth = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    employment_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    retirement_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    class Meta:
        model = Employee
        fields = ('first_name','last_name','other_name','date_of_birth','state_of_origin','lga_of_origin','employment_date','retirement_date','photograph','email','phone',)


class EmployeeDepartmentCreateForm(forms.ModelForm):
    date_added = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    class Meta:
        model = EmployeeDepartment
        fields = ('employee','department','date_added')
        widgets = {"employee": forms.HiddenInput()}

class EmployeePositionCreateForm(forms.ModelForm):
    start_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    class Meta:
        model = EmployeePosition
        fields = ('employee','position','start_date')
        widgets = {"employee": forms.HiddenInput()}

class EmployeeLeaveCreateForm(forms.ModelForm):
    start_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    class Meta:
        model = EmployeeLeave
        fields = ('employee','leave','start_date')
        widgets = {"employee": forms.HiddenInput()}