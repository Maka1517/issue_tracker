from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseNotAllowed
from django.urls import reverse, reverse_lazy
from django.utils.timezone import make_naive
from django.views.generic import View, TemplateView, CreateView, UpdateView, DeleteView

from webapp.models import Issue
from webapp.forms import IssuesForm, BROWSER_DATETIME_FORMAT


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

@login_required
def my_view(request):
    return HttpResponse('Hello!')


class IssueView(TemplateView):
   template_name = 'view.html'
   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)

       pk = self.kwargs.get('pk')
       issue = get_object_or_404(Issue, pk=pk)

       context['issue'] = issue
       return context


class IssueCreatView(LoginRequiredMixin, CreateView):
    template_name = 'issue_create.html'
    model = Issue
    fields = ['summary', 'description', 'status', 'issue_type']

    def get_success_url(self):
        return reverse('issue_view', kwargs={'pk': self.object.pk})


class IssueUpdateView(LoginRequiredMixin, UpdateView):
    model = Issue
    template_name = 'issue_update.html'
    form_class = IssuesForm
    context_object_name = 'issues'

    def get_success_url(self):
        return reverse('issue_view', kwargs={'pk': self.object.pk})


class IssueDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'issue_delete.html'
    model = Issue
    context_object_name = 'issues'
    success_url = reverse_lazy('index')




