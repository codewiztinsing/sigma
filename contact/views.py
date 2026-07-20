from django.shortcuts import render

from .models import ContactMessage


def contact(request):
    context = {'active_page': 'contact'}

    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        subject = request.POST.get('subject', '').strip()
        message = request.POST.get('message', '').strip()

        valid_subjects = dict(ContactMessage.SUBJECT_CHOICES)
        errors = []
        if not name:
            errors.append('Full name is required.')
        if not email:
            errors.append('Email address is required.')
        if subject not in valid_subjects:
            errors.append('Please select a valid subject.')
        if not message:
            errors.append('Message is required.')

        if errors:
            context['errors'] = errors
            context['form_data'] = {
                'name': name,
                'email': email,
                'phone': phone,
                'subject': subject,
                'message': message,
            }
        else:
            ContactMessage.objects.create(
                name=name,
                email=email,
                phone=phone,
                subject=subject,
                message=message,
            )
            context['success'] = True

    return render(request, 'contact.html', context)
