# from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse

import json

class IndexView(View):

    def post(self, request):

        data = json.loads(request.body).get('data')

        event_title = data.get('title')
        event_description = data.get('description')
        event_link = data.get('link')
        event_emails = data.get('emails')

        for email in event_emails:
            pass

        return JsonResponse({'message': 'success'})