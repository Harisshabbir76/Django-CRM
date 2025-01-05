from .models import Register
from django import forms

class Register_user(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['first_name', 'last_name', 'phone_number', 'age', 'address', 'position', 'salary']

    def __init__(self, *args, **kwargs):
        super(Register_user, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'  
            field.widget.attrs['placeholder'] = field.label
            field.label = ''  
