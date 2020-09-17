from django.urls import path
from .views import IndexView, IssueCreatView, IssueView, IssueUpdateView, IssueDeleteView

app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('issue/<int:pk>/', IssueView.as_view(), name='issue_view'),
    path('issue/add/', IssueCreatView.as_view(), name='issue_create'),
    path('issue/<int:pk>/update/', IssueUpdateView.as_view(),name='issue_update'),
    path('issue/<int:pk>/delete/', IssueDeleteView.as_view(), name='issue_delete')
]