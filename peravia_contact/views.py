from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages
from .models import Contact, WriteUs
from peravia_setting.models import SiteSetting , SocialMedia


# ----------------------------------------------------------
def contact_us_page(request):
    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            fullname = contact_form.cleaned_data.get('fullname')
            email = contact_form.cleaned_data.get('email')
            phone_number = contact_form.cleaned_data.get('phone_number')
            subject = contact_form.cleaned_data.get('subject')
            enquiry = contact_form.cleaned_data.get('enquiry')
            Contact.objects.create(
                fullname=fullname,
                email=email,
                phone_number=phone_number,
                subject=subject,
                enquiry=enquiry)
            messages.success(request, 'We will be in touch soon')
            return redirect('/')
        messages.error(request, 'Something went wrong')
    form = ContactForm()
    return render(request, 'contact/Contact_Us_Page.html',
                  context={'contact_form': form,
                           'page_name': 'Contact Us',
                           'title': 'Peravia | Contact Us',
                           'settings': SiteSetting.objects.first(),
                           'social_media': SocialMedia.objects.all()})

# ----------------------------------------------------------
def write_us(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        phone = request.POST.get('phone_number')
        message = request.POST.get('message')
        WriteUs.objects.create(
            fullname=fullname,
            phone=phone,
            message=message
        )
        messages.success(request, 'We will call you back')
        return redirect('/')
    messages.error(request, 'Something went wrong')
    return redirect('/')
