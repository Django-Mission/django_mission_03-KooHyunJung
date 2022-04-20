from django.db import models

# Create your models here.

# 중복 기본 필드 상속 [최종 수정일시, 생성일시] 
class BaseModel(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True