from cheatingdash.models import Employee
import django_filters



class employeeFilter(django_filters.FilterSet):
    class Meta:
        model = Employee
        fields = '__all__'
