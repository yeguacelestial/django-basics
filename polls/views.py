from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Question

# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5] # Reverse order by publication date
    stuff_for_frontend = {
        'latest_question_list': latest_question_list,
    }
    output = ', '.join([q.question_text for q in latest_question_list])
    return render(request, 'polls/index.html', stuff_for_frontend)

# More views...
# A request is passed whenever you do anything

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s" % question_id)

