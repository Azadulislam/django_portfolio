from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives, send_mail
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.urls import resolve, reverse
from django.utils.html import strip_tags

from .forms import ContactForm
from .models import (Administrator, Portfolio, Services, SiteSetting, Skill,
                     Summery, Testimonial, WonerTitle)

pages = ['profile', 'portfolio']
portfolios = Portfolio.objects.all()


def index(request):
    portfolios = Portfolio.objects.all()
    administrator = Administrator.objects.all()[0]
    site = SiteSetting.objects.all()[0]
    try:
        skills = Skill.objects.all()
        services = Services.objects.all()
        testimonials = Testimonial.objects.all()
        
        titles = WonerTitle.objects.all()
        site = SiteSetting.objects.all()[0]
        summerys = Summery.objects.all()[0]
    except IndexError:
        return HttpResponse('Create Object for administrator')

    title = 'Home - Azadul islam'
    # contact_form = ContactForm()
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            try:
                # send_mail(
                #     subject,
                #     message,
                #     email,
                #     [getattr(settings, "EMAIL_HOST_USER", None)],
                #     fail_silently=False,
                # )

                # Html mail sending
                mail_title = name + " Send a message"
                html_content = render_to_string('mail/contact_us.html', {'title':mail_title, 'message':message})
                text_content = strip_tags(html_content)
                email = EmailMultiAlternatives(
                    subject,
                    text_content,
                    email,
                    [settings.EMAIL_HOST_USER]
                )
                email.attach_alternative(html_content, 'text/html')
                email.send()

                messages.success(request,"Mail Send success Fully")
            except TimeoutError:
                messages.error(request,"Sending message time out please try again")
        else:
            for field in contact_form.errors:
                contact_form[field].field.widget.attrs['class'] += ' is-invalid'
    else: 
        contact_form = ContactForm()
    context = {
        "admin":administrator,
        "skills":skills,
        "title":title, 
        "services":services, 
        "testimonials": testimonials, 
        "portfolios": portfolios,
        "summerys": summerys,
        "site": site,
        "contact_form": contact_form,
        "titles": titles
        }
    return render(request, 'index.html', context)

def contact(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        pass
    else:
        next = request.GET.get('next', reverse('home'))
        return redirect(next)

def profile(request):
    current_url = resolve(request.path_info).url_name
    administrator = Administrator.objects.all()[0]
    site = SiteSetting.objects.all()[0]
    
    
    if current_url in pages:
        class_name = 'bg-dark'
    else:
        class_name = ''
    title = "Profile"
    context = {
        'class_name' : class_name,
        'admin': administrator,
        "site": site,
        "title":title, 
    }
    return render(request, 'about.html', context)

def portfolio(request):
    current_url = resolve(request.path_info).url_name
    administrator = Administrator.objects.all()[0]
    site = SiteSetting.objects.all()[0]
    if current_url in pages:
        class_name = 'bg-dark'
    else:
        class_name = ''
    title = "Portfolios"
    context = {
        "title":title, 
        'class_name' : class_name,
        'admin': administrator,
        "site": site,
        'portfolios' : portfolios,
    }
    return render(request, 'portfolio.html', context)


def view_404(request, exception):
    return render(request, 'error-404.html')

def view_500(request, template_name="error-500.html"):
    return render(request, template_name)

def view_400(request, exception):
    return render(request, 'error-400.html')
