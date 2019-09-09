from django.shortcuts import get_object_or_404, render
from django .http import HttpResponseRedirect
from .forms import ContactForm
from django.core.mail import send_mail, get_connection
from datetime import date
import calendar
from calendar import HTMLCalendar



def contact(request):
    submitted = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            assert False
            con = get_connection('django.core.mail.backends.console.EmailBackend')
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', ''),
                      ['webd@gmail.com'],
                connection=con
             )
            return HttpResponseRedirect('/contact?submitted=True')
            
    else:
            form = ContactForm()
            if 'submitted' in request.GET:
                submitted = True
                

    return render(request, 'contact.html',{'form':form,'submitted':submitted})


     
    
    