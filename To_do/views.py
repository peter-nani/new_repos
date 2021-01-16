from django.shortcuts import render,redirect
from django.http import HttpResponse, request
from .forms import do_it_f
from .models import To_Do
# Create your views here.
def home(request):
    #through the form in to your views
    ob_to = To_Do.objects.all()
    form = do_it_f()
    context = {'form':form,'ob_to':ob_to}
    if request.method == 'POST':
        form = do_it_f(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'home.html',context,)
def obj_edit(request,id):
    #get the id from request
    get_item = To_Do.objects.get(id=id)
    #create the same form instance
    form = do_it_f(instance=get_item)
    #save the data that populated in the form
    if request.method == 'POST':
        form = do_it_f(request.POST,instance=get_item)
        if form.is_valid():
            form.save()
            return redirect('/')
    #create a context that you want to display
    context = {'form': form}
    #display the context along with the template.
    return render(request,'home.html',context)
def delet(request,id):
    item = To_Do.objects.get(id=id)
    item.delete()
    return redirect('/')