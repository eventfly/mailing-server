# from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.views import View
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives, send_mail
from django.http import JsonResponse

from mailingserver.settings import EMAIL_HOST_USER

import json

class IndexView(View):

    # Sample POST Data:
    # 
    # {
    #     "data": {
    #         "title": "Event Title",
    #         "description": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
    #         "banner": "https://images.pexels.com/photos/976866/pexels-photo-976866.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500",
    #         "link": "https://www.google.com",
    #         "emails": [
    #             "a@b.c",
    #             "d@e.f"
    #         ]
    #     }
    # }

    def post(self, request):

        data = json.loads(request.body).get('data')

        context = {
            'event_title': data.get('title'),
            'event_description': data.get('description'),
            'event_banner': data.get('banner'),
            'event_link': data.get('link')
        }

        html_content = get_template('core/email.html').render(context)
        text_content = str(html_content)

        # print(text_content)

        # return HttpResponse(text_content)

        subject = "[EventFly] Invitation for " + context['event_title']
        from_email = EMAIL_HOST_USER
        to = data.get('emails')

        msg = EmailMultiAlternatives(subject, text_content, from_email, to)
        msg.attach_alternative(html_content, "text/html")
        msg.send(fail_silently=False)

        return JsonResponse({'message': 'success'})