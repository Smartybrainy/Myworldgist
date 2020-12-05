from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.utils import timezone

from .models import EmailList


def index_view(request):
    map_access_token = 'pk.eyJ1Ijoic21hcnR5YnJhaW55IiwiYSI6ImNrZzdzemh3dzBhZGUycW52MXFkemsyaXAifQ.VVUcjKN3yEwtVYM6TqCgdA'
    context = {
        'map_access_token': map_access_token,
    }
    return render(request, 'core/index.html', context)


@csrf_exempt
def create_email_list(request):
    if request.method == 'POST':
        name = request.POST['username']
        email = request.POST['email']
        created_date = timezone.now()
        created_emails = EmailList.objects.create(
            name=name, email_address=email, created_date=created_date)
        created_emails.save()
        messages.success(
            request, 'Email subscription created successfully, check your email before 24hrs to complete regitration.')
        return redirect('core:index')
    return redirect('core:index')
