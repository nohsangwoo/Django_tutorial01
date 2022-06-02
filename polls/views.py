from django.template import loader
from django.http import HttpResponse
from polls.models import Question
from django.shortcuts import get_object_or_404, render


def test(request):
    return HttpResponse("It's a test.")


def index(request):
    # [:5] : 최근 5개를 뽑아와라
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)



def detail(request, question_id):
    # 에러 핸들링(DB에 없는 값을 가져올때 에러핸들링)
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
