from django.shortcuts import render
from myApp.models import Student
from myApp.forms import StudentForm

# Create your views here.
def input_view(request):
	f=StudentForm()
	if request.method=="POST":
		f=StudentForm(request.POST)
		if f.is_valid():
			f.save(commit=True)
	return render(request,'myApp/1.html',{'form':f})
