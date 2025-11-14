from django.shortcuts import render
from formapp.forms import StudentForm

# Create your views here.
def index(request):
    form= StudentForm()
    if request.method =='POST':
      form = StudentForm(request.POST)
      if form.is_valid():
         print("validation success")
        #  print(form.cleaned_data['name'])
        #  print(form.cleaned_data['age'])
         form.save()
    return render(request,"index.html",{'form':form})
