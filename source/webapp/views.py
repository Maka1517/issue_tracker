from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotAllowed
from django.utils.timezone import make_naive
from django.views.generic import View, TemplateView

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

class IssueView(TemplateView):
   template_name = 'view.html'
   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)

       pk = self.kwargs.get('pk')
       issue = get_object_or_404(Issue, pk=pk)

       context['issue'] = issue
       return context


class IssueCreatView(View):
    def get(self,request):
        return render(request,'issue_create.html', context={'form':IssuesForm()})

    def post(self,request):
        form = IssuesForm(data=request.POST)
        if form.is_valid():
            issue = Issue.objects.create(
                summary=form.cleaned_data['summary'],
                description=form.cleaned_data['description'],
                status=form.cleaned_data['status'],
                issue_type=form.cleaned_data['issue_type'],
                created_at=form.cleaned_data['created_at']
            )
            return redirect('issue_view', pk=issue.pk)
        else:
            return render(request,'issue_create.html', context={'form': form})


