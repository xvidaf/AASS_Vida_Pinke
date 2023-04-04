from django.shortcuts import render

from EntityProvider.forms import TeacherForm



# Create your views here.

def teacherCreation(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TeacherForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
    else:
        form = TeacherForm()

    return render(request, "createSubject.html", {'form': form})