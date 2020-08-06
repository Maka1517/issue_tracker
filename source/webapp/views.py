from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotAllowed
from django.utils.timezone import make_naive
from django.views.generic import View, TemplateView

from webapp.models import Issue
#from webapp.forms import ArticleForm, BROWSER_DATETIME_FORMAT


class IndexView(View):
    def get(self, request):
        is_admin = request.GET.get('is_admin', None)
        if is_admin:
            data = Issue.objects.all()
        else:
            data = Issue.objects.all()
        return render(request, 'index.html', context={
            'issues': data
        })


