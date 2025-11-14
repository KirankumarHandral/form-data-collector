from django import forms
from formapp.models import Student


class StudentForm(forms.ModelForm):
     
    # name = forms.CharField(max_length=100)
    # age = forms.IntegerField()
    # phone = forms.IntegerField()
    # address = forms.CharField(max_length=250)

    # def clean_name(self):
    #     name = self.cleaned_data['name']
    #     if ord(name[0])>=40 and ord(name[0])<=50:
    #         raise forms.ValidationError('name started with characters not number')
    #     return name
    # def clean_age(self):
    #     age = self.cleaned_data['age']
    #     # if 1>=65 and ord(age[0])<=126:
    #     if age <= 0:
            
    #         raise forms.ValidationError('age not negitive')
    #     return age
     class Meta:
        model = Student
        fields = '__all__'
