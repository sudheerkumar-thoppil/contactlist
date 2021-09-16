from django.shortcuts import render, HttpResponseRedirect
from .models import Phonebook
from .forms import PhoneContacts

# Create your views here.
def addcontact(request):
    if request.method == 'POST':
        pm = PhoneContacts(request.POST)
        if pm.is_valid():
            pm.save()
            pm = PhoneContacts()
    else:
        pm = PhoneContacts()
    contacts = Phonebook.objects.all()
    return render(request, 'contact/addcontact.html',{'form':pm,'contacts':contacts})

def delete_data(request, id):
    if request.method == "POST":
        pi=Phonebook.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

def updatedata(request, id):
    if request.method == "POST":
        pi= Phonebook.objects.get(pk=id)
        pm= PhoneContacts(request.POST,instance=pi)
        if pm.is_valid():
            pm.save()
        else:
            pi = Phonebook.objects.get(pk=id)
            pm =PhoneContacts(instance=pi)
    return render(request,'contact/updatecontact.html',{'form':pm})
        




