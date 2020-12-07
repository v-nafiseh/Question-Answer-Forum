from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.utils import timezone
from . import models
from django.http import HttpResponse
from .forms import DisplayForm


def index(request):

    questions = models.Question.objects.filter(status='published')

    for q in questions:
        answers = models.Answer.objects.filter(question_id = q.id)
        categories = q.categories.all()

    context = {'questions':questions, 'answers':answers, 'categories':categories}

    return render(request, 'questions/index.html', context)



def ask_question(request):

    # if request.method == "POST":
        form = DisplayForm(request.POST)
        # if form.is_valid():
        #     post = form.save(commit=False)
        #     post.author = request.user
        #     post.published_date = timezone.now()
        #     post.save()
        #     return redirect('questions/index.html', pk=post.pk)
        # else:
        return render(request, 'questions/ask.html', {'form':form})    


def question_detail(request, q_id):

    question = models.Question.objects.get(id=q_id)
    answers = question.answer_set.all()

    context = {
        'question':question,
        'answers':answers,
    }

    return render(request, 'questions/question_detail.html', context)

def about_us(request):
    return HttpResponse("this is about us")

def contact(request):
    return HttpResponse("contact page") 
           