# from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.views import View
from django.template.loader import get_template
from django.http import JsonResponse

import json

class IndexView(View):

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

        return HttpResponse(text_content)

        event_emails = data.get('emails')

        for email in event_emails:
            # Send mail with text_content to email
            pass

        return JsonResponse({'message': 'success'})