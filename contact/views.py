import requests
from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from .forms import ContactForm

def contact(request):

  if request.method == 'POST':
    form = ContactForm(request.POST)
    if form.is_valid():

      ''' Begin reCAPTCHA validation '''
      recaptcha_response = request.POST.get('captcha')
      params = {
        'secret': settings.RECAPTCHA_SECRET_KEY,
        'response': recaptcha_response,
      }

      r = requests.post('https://www.google.com/recaptcha/api/siteverify?', data=params, verify=True)
      result = r.json()
      ''' End reCAPTCHA validation '''
      
      if result['success']:
        full_name = form.cleaned_data['full_name']
        subject = form.cleaned_data['subject']
        from_email = form.cleaned_data['from_email']
        message = form.cleaned_data['message']
        try:
          final_form = "Full Name: " + full_name + "\n\n" + "From: " + from_email + "\n\n" + message
          send_mail(subject, final_form, 'eribe403@gmail.com', ['eribe403@gmail.com'], fail_silently=False)
        except BadHeaderError:
          return HttpResponse('Invalid header found.')
        return redirect('success')

      else:
        messages.error(request, 'Invalid reCAPTCHA. Please try again.')
        return redirect('/contact#email')

    messages.error(request, 'Enter correct form information')
    return redirect('/contact#email')

  # GET     
  else:
    form = ContactForm()
    return render(request, "contact/contact.html", {'form': form})

def success(request):
    return render(request, "contact/success.html")