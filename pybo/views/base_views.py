from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from ..models import Question

from django.db.models import Q

# GJ for searching with the search key words, and order
from django.db.models import Count

def index(request):
    # GJ Error for Log Test
    print("Before DivZero Error GJ")
    3/0
    #print("After DivZero Error GJ")
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어

    # GJ for sorting
    #so = request.GET.get('so', 'recent')
    so = request.GET.get('so', '')

    if so == 'recommend':
        question_list = Question.objects.annotate(
            num_voter=Count('voter')).order_by('-num_voter', '-create_date')
    elif so == 'popular':
        question_list = Question.objects.annotate(
            num_answer=Count('answer')).order_by('-num_answer', '-create_date')
    else:
        question_list = Question.objects.order_by('-create_date')
    # GJ for sorting
    #question_list = Question.objects.order_by('-create_date')

    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |  # 제목 검색
            Q(content__icontains=kw) |  # 내용 검색
            Q(answer__content__icontains=kw) |  # 답변 내용 검색
            Q(author__username__icontains=kw) |  # 질문 글쓴이 검색
            Q(answer__author__username__icontains=kw)  # 답변 글쓴이 검색
        ).distinct()

    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    #context = {'question_list': page_obj}
    #context = {'question_list': question_list}

    #GJ for search
    #context = {'question_list': page_obj, 'page': page, 'kw': kw}

    # GJ for search and order
    context = {'question_list': page_obj, 'page': page, 'kw': kw, 'so': so}



    #return HttpResponse("안녕하세요. Django에 오신 것을 환영합니다.")
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    #question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)

#def answer_create(request, question_id):
#    question = get_object_or_404(Question, pk=question_id)
#    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
#    return redirect('pybo:detail', question_id=question.id)
