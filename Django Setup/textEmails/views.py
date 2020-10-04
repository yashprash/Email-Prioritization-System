
from django.shortcuts import render, redirect, render_to_response
from django.views.generic import TemplateView
from textEmails.models import *
import requests as requestinghttps
import datetime
import json

# Create your views here.


class AboutView(TemplateView):
    template_name = 'textEmails/about.html'


class InboxView(TemplateView):
    template_name = 'textEmails/mailbox.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mail = Email.objects.all().order_by('-date')
        context['mails'] = mail
        return context



def HomeView(request):
    mail = Email.objects.all().order_by('-date')
    pri1 = request.session['pri1']
    pri2 = request.session['pri2']
    pri3 = request.session['pri3']

    return render(request, 'textEmails/home.html', {'priority1': pri1, 'priority2': pri2, 'priority3': pri3, 'mails': mail})


class ContactUsView(TemplateView):
    template_name = 'textEmails/contactus.html'


def P1View(request):
    pri1 = request.session['pri1']
    pri2 = request.session['pri2']
    pri3 = request.session['pri3']
    mail = Email.objects.filter(priority__icontains=pri1).order_by('-date')
    number_p1 = Email.objects.filter(priority__icontains=pri1).count()

    return render(request, 'textEmails/priority1.html', {'number1': number_p1, 'priority1': pri1, 'priority2': pri2, 'priority3': pri3, 'mails': mail})


def P2View(request):
    pri1 = request.session['pri1']
    pri2 = request.session['pri2']
    pri3 = request.session['pri3']
    mail = Email.objects.filter(priority__icontains=pri2).order_by('-date')
    number_p2 = Email.objects.filter(priority__icontains=pri2).count()

    return render(request, 'textEmails/priority2.html', {'number2': number_p2, 'priority1': pri1, 'priority2': pri2, 'priority3': pri3, 'mails': mail})


def P3View(request):
    pri1 = request.session['pri1']
    pri2 = request.session['pri2']
    pri3 = request.session['pri3']
    mail = Email.objects.filter(priority__icontains=pri3).order_by('-date')
    number_p3 = Email.objects.filter(priority__icontains=pri3).count()

    return render(request, 'textEmails/priority3.html', {'number3': number_p3, 'priority1': pri1, 'priority2': pri2, 'priority3': pri3, 'mails': mail})


def sendmail(request):
    pri1 = request.session['pri1']
    pri2 = request.session['pri2']
    pri3 = request.session['pri3']
    mail = Email.objects.all().order_by('-date')

    if request.method == 'POST':
        from_name = request.POST.get('sender_name')
        to_mail = "suhasagasthya@gmail.com"
        from_mail = request.POST.get('email')
        to_name = "Suhas Agasthya"
        subject = request.POST.get('subject')
        mail_body = request.POST.get('content')
        categ = requestinghttps.get(url='http://ec2-54-162-218-173.compute-1.amazonaws.com:5000/run_model', params={'mails': mail_body})
        ans = categ.json()
        category = json.loads(ans)
        print(category)

        dates = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        try:
            db = Email.objects.create(from_mail=from_mail,
                                      to_mail=to_mail,
                                      from_name=from_name,
                                      to_name=to_name,
                                      subject=subject,
                                      body=mail_body,
                                      date=dates,
                                      priority=category)
            db.save()
        except:
            print()

        return render(request, 'textEmails/home.html', {'priority1': pri1, 'priority2': pri2, 'priority3': pri3, 'mails': mail})

    else:
        return render(request, 'textEmails/home.html', {'priority1': pri1, 'priority2': pri2, 'priority3': pri3, 'mails': mail})


def priority_select(request):
    if request.method == 'POST':
        mail = Email.objects.all().order_by('-date')
        pri1 = request.POST.get('priority1')
        pri2 = request.POST.get('priority2')
        pri3 = request.POST.get('priority3')
        request.session['pri1'] = pri1
        request.session['pri2'] = pri2
        request.session['pri3'] = pri3
        return render(request, 'textEmails/home.html', {'priority1': pri1, 'priority2': pri2, 'priority3': pri3, 'mails': mail})











