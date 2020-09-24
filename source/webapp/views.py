from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseNotAllowed
from django.urls import reverse, reverse_lazy
from django.utils.timezone import make_naive
from django.views.generic import View, TemplateView, CreateView, UpdateView, DeleteView, DetailView, ListView

from webapp.models import Issue
from webapp.forms import IssuesForm, BROWSER_DATETIME_FORMAT


class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'issues'
    paginate_by = 4
    paginate_orphans = 2
    model = Issue
    ordering = ['created_at']

    # def get_queryset(self):
    #     data = super().get_queryset()
    #     if not self.request.GET.get('is_admin', None):
    #         data = data.filter(status='moderated')
    #     return data



@login_required
def my_view(request):
    return HttpResponse('Hello!')


class IssueView(DetailView):
   template_name = 'view.html'
   model = Issue
   # def get_context_data(self, **kwargs):
   #     context = super().get_context_data(**kwargs)
   #
   #     pk = self.kwargs.get('pk')
   #     issue = get_object_or_404(Issue, pk=pk)
   #
   #     context['issue'] = issue
   #     return context


class IssueCreatView(PermissionRequiredMixin, CreateView):
    template_name = 'issue_create.html'
    model = Issue
    fields = ['summary', 'description', 'status', 'issue_type']
    permission_required = 'webapp.change_issue'

    def has_permission(self):
        return super().has_permission() or self.get_object().author == self.request.user

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:issue_view', kwargs={'pk': self.object.pk})


class IssueUpdateView(PermissionRequiredMixin, UpdateView):
    model = Issue
    template_name = 'issue_update.html'
    form_class = IssuesForm
    context_object_name = 'issues'
    permission_required = 'webapp.change_issue'

    def has_permission(self):
        return super().has_permission() or self.get_object().author == self.request.user

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('issue_view', kwargs={'pk': self.object.pk})


class IssueDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'issue_delete.html'
    model = Issue
    context_object_name = 'issues'
    success_url = reverse_lazy('index')
    permission_required = 'webapp.delete_issue'




