from django.contrib import admin
from polls.models import Question, Choice


class ChoiceInline(admin.TabularInline):#테이블 형식으로 Choice를 Question도메인에서 보여줌
    model = Choice
    extra = 2 #기존것 제외하고 추가 choice개수

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [('Question Statement',{'fields':['question_text'],'classes':['collapse']}),
                ('Date Information',{'fields':['pub_date'],'classes':['collapse']}),] #필드를 분리해서 보여주기
           #순서대로     필드 제목          field: 필드명

    inlines = [ChoiceInline]  #Choice를 Question안으로 들어가게함
    list_display = ('question_text', 'pub_date') #레코드 리스트 컬럼 지정
    list_filter = ['pub_date'] #필드에 따른 filer생성
    search_fields = ['question_list'] #검색 박스


admin.site.register(Question,QuestionAdmin) #어드민 페이지에 등록
admin.site.register(Choice)


# Register your models here.

