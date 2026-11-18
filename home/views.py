from django.shortcuts import render ,  HttpResponse
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def index(request):
    if request.method == "POST":
        mail =  request.POST.get('mail')
        desc  =  request.POST.get('desc')
        # print(mail,desc)
        send_mail(
            f"hie ",# subject 
            f"Your Complaint \n{desc}\nhas been Noted \nOur Team will reach you soon\nRegards\nHelp Team,", # body
            settings.EMAIL_HOST_USER, # sender mail
            [mail],# receiver mail
            fail_silently=True
        )
        return HttpResponse("mail sent")
    return render(request,"index.html")
