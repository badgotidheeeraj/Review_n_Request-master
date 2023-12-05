from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import UserAccount
from datetime import datetime

class MasterModule(models.Model):
    module_name = models.CharField(max_length=200)
    json_field = models.JSONField()

    def __str__(self):
        return self.module_name


class RequestModule(models.Model):
    username = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    ModuleName = models.ForeignKey(MasterModule, verbose_name=_("Module Name"), on_delete=models.CASCADE)
    request_name = models.CharField(max_length=1000, blank=True, null=True)
    json_field = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(default=datetime.now)
    is_favorite = models.BooleanField(default=False)


    def __str__(self):
        return self.request_name


class Resource(models.Model):
    json_field = models.JSONField()

    def __str__(self) -> str:
        return super().__str__()


class ReviewModule(models.Model):
    username = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    request_name= models.CharField(max_length=255) 
    review_name = models.CharField(max_length=255, null=True, blank=True)
    docx_file = models.FileField(upload_to='documents/', null=True, blank=True)
    processed_file = models.JSONField(null=True, blank=True)
    json_field = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(default=datetime.now)
    review_type = models.CharField(max_length=255)
    is_favorite = models.BooleanField(default=False)



    def __str__(self):
        return self.review_name
