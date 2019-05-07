from django.db import models
from django import forms

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length = 50)
    movie = models.CharField(max_length = 200, null=True)
    genre = models.CharField(max_length = 200, null=True)
    description = models.TextField(null=True)
    
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
# 이런식으로 null=True 옵션을 주면 해당 컬럼 값이 비어있어도 괜찮음 views.py 로 오삼.

    def __str__(self):
        return self.name
        
# __str__ : product가 보이는 것의 함수. 덮어쓰기를 하는 것임.