from django.shortcuts import render
from .models import Question, Answer
from django.core.paginator import Paginator
# Home Page 
def home(request):
    if 'q' in request.GET:
    	q=request.GET['q']
    	quests=Question.objects.filter(title__icontains=q).order_by('-id')
    else:
        quests=Question.objects.all().order_by('-id')
    paginator=Paginator(quests,1)
    page_num=request.GET.get('page',1)
    quests=paginator.page(page_num)
    return render(request,'home.html',{'quests':quests})

#Detail
def detail(request,id):
    quest=Question.objects.get(pk=id)
    tags=quest.tags.split(',')
    answer=Answer.objects.get(question=quest)
    return render(request,'detail.html',{'quest':quest,'tags':tags})