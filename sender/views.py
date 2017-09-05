
from django.shortcuts import render
from sender.forms import SendMailForm
from django.core.mail import send_mail
from sender.models import message
from django.http import HttpResponseRedirect
from django.conf import settings
from random import randint





def index(request):
	if request.method == 'POST':
		form = SendMailForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			to = form.cleaned_data['email']
			messageList = message.objects.all()
			subject = 'Hello ' + name
			k=randint(0,len(messageList)-1)
			send_mail(subject,messageList[k].text, settings.EMAIL_HOST_USER,
         [to], fail_silently=False)
			return render(request,'sender/thanks.html')
	else:
		form = SendMailForm()
		return render(request,'sender/index.html',{'form':form})
