from django.shortcuts import render, redirect
from ..form import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry"
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'shubham.joshi1507@gmail.com',
                          ['shubham.joshi1507@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect("homepage")

    form = ContactForm()
    return render(request, "contact.html", {'form': form})
