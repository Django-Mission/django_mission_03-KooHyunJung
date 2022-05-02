from django.contrib import admin

from support.models import Inquiry, Answer

# Register your models here.

# admin.site.register(Inquiry)
# admin.site.register(Answer)

class AnswerInline(admin.TabularInline):
    model = Answer
    min_num = 1
    verbose_name="설문 질문 항목"


@admin.register(Inquiry)
class InquiryModelAdmin(admin.ModelAdmin):
    list_display = ('title','category','created_by_id','created_at')
    search_fields = ('title', 'email', 'phone')
    search_help_text = '[제목, 이메일, 전화번호] 항목으로 검색 가능합니다'
    inlines = [AnswerInline]