from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)

    customer_name = models.CharField(max_length=200,default='')         #取引先名
    project_title = models.CharField(max_length=200,default='')         #案件名
    contract = models.CharField(max_length=200,default='')              #契約、勤務形態
    overview = models.TextField(default='')                             #概要
    period = models.CharField(max_length=200,default='')                #期間
    current_process = models.CharField(max_length=200,default='')       #現行工程
    status_status = models.CharField(max_length=200,default='')         #状況ステータス
    situation_details = models.TextField(default='')                    #状況詳細
    person = models.CharField(max_length=200,default='')                #責任者、PM、リーダー
    contact_information = models.CharField(max_length=200,default='')   #問い合わせ先
    unit_price = models.CharField(max_length=200,default='0')           #受注額、単価
    business_trip = models.CharField(max_length=200,default='')         #出張の有無
    one_word_appeal = models.CharField(max_length=600,default='')       #一言アピール

    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title