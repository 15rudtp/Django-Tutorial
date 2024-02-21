from django.conf import settings
from django.db import models
from django.utils import timezone
# Create your models here.

"""
@models : 장고 모델임을 의미함. 이 코드로 인해 DB와 매핑 됨.

----DB의 필드 타입 정의
    * CharField : 글자 수가 제한된 텍스트
    * TextField : 글자 수 제한이 없는 텍스트
    * DateTimeField : 날짜와 시간
    * ForeignKey : 참조키
"""


class Post (models.Model) : 
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length = 200)
    text = models.TextField()
    created_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank = True, null = True)

    def publish(self) : 
        self.published_date = timezone.now()
        self.save()

    def __str__(self) :
        return self.title