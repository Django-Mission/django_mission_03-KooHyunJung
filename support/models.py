from django.db import models
from config.models import BaseModel
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth import get_user_model

User = get_user_model()

# 모델 구성
# BaseModel 상속 - [최종 수정일시, 생성일시] 중복 필드
# Inquiry 카테고리, 타이틀, 이메일, 이메일체크, 번호, 번호체크, 내용, 생성자, 이미지, [최종 수정일시, 생성일시]
# Answer 답변 내용, 참조 문의글, 생성자 [최종 수정 일시, 생성 일시]

class Inquiry(BaseModel):
    CATEGORY_CHOICE = (
        ('NR', '일반'),
        ('AC', '계정'),
        ('Et', '기타'),
    )
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICE, verbose_name="문의 카테고리")
    title = models.CharField(max_length=100, verbose_name="제목")
    email = models.EmailField(max_length=128, blank=True, verbose_name="작성자 이메일") # blank=True 빈 값 허용
    is_eamil = models.BooleanField(blank=True, null=True, verbose_name="답변 수신을 이메일로 받겠습니다.") # 빈 값 허용, NullBooleanField 더 이상 사용 안 함.
    phone = PhoneNumberField(blank=True, null=True, verbose_name="작성자 전화번호") # Google libphonenumber 라이브러리 포트. 전화번호 유효성 검사, 국제적 표준양식
    is_phone = models.BooleanField(blank=True, null=True, verbose_name="답변 수신을 문자메시지로 받겠습니다.") # 빈 값 허용, NullBooleanField 더 이상 사용 안 함.
    content = models.TextField(verbose_name="내용")
    created_by_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name="질문 작성자")
    image =  models.ImageField(upload_to="Inquiry/%Y%m%d", blank=True, max_length=255, verbose_name="이미지 파일 업로드") # 빈 값 허용


class Answer(BaseModel):
    # Django OneToManyField : ForeignKey 사용
    inquiry_id = models.ForeignKey(Inquiry, on_delete=models.CASCADE, db_column="inquiry_id", verbose_name="참조 문의글")
    answer = models.TextField(verbose_name="답변 내용")
    updated_by_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name="답변 작성자")
