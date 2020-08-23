from django.db import models
from django.utils import timezone

STATUS_CHOICES = [
    ('new', 'Новый'),
    ('in progress', 'В процессе'),
    ('done', 'Выполнено')
]

class Status(models.Model):
    status_name = models.CharField(max_length=50, choices=STATUS_CHOICES, verbose_name='Статус')

    def __str__(self):
        return self.status_name[:20]

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

TYPE_CHOICES = [
('task', 'Задача'),
('bug', 'Ошибка'),
('enhancement', 'Улучшение')
]

class IssueType(models.Model):
    issue_type = models.CharField(max_length=15, choices=TYPE_CHOICES, verbose_name='Статус')

    def __str__(self):
        return self.issue_type[:20]

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'

class Issue(models.Model):
    summary = models.CharField(max_length=200, null=False, blank=False, verbose_name='Заголовок')
    description = models.TextField(max_length=3000,  verbose_name='Описание')
    status = models.ForeignKey('webapp.Status', related_name='status',
                                on_delete=models.PROTECT, verbose_name='Статус')
    issue_type =models.ForeignKey('webapp.IssueType', related_name='type',
                                on_delete=models.PROTECT, verbose_name='Тип')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')



    def __str__(self):
        return "{}. {}. {}".format(self.summary, self.status,self.issue_type)

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'



