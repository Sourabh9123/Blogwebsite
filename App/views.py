from django.shortcuts import render, redirect
from App.models import Content
from App.email_send import send_email
from django.db.models import Q



# https://devmaesters.com/blog/15   # configure of versel on website


def home(request):
    content = None
    if request.method == "POST":
        content = request.POST['itemtofound']
        if content:
            try:
                article = Content.objects.filter(Q(content__icontains=content) | Q(header__icontains=content))

                
                length = len(article)
                print(article, length)
                context = {
                        'articles':article,
                        'length':length }

            except Exception as e:
                print(e)
                article = Content.objects.all().order_by('-created_at')
                length = len(article)
                

        
    if not content:
        article = Content.objects.all().order_by('-created_at')
        length = len(article)
        print('____________________________--------------')
        
        context = {
            'articles':article,
            'length':length

        }
    return render(request, 'home.html',context)


def aboutus(request):

    return render(request, 'aboutus.html')

from django.shortcuts import redirect

def contactus(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        # Check if email has already been sent during this session
        if not request.session.get('email_sent', False):
            sender_email = 'sourabhd081@gmail.com'
            sender_password = 'pwcufkkzqeperjda'
            recipient_email = email
            subject = name
            body = message

            send_email(sender_email, sender_password, recipient_email, subject, body)
            message = 'success'
            # Set the email_sent session variable to True to indicate the email has been sent
            request.session['email_sent'] = True

        return render(request, 'contactus.html', {'success':message})
    else:
        # Clear the email_sent session variable if it exists
        if 'email_sent' in request.session:
            del request.session['email_sent']

        return render(request, 'contactus.html')
    





def terms(request):
    return render(request, 'terms.html')




