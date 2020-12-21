from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.utils import timezone
from .models import Question, Answer, Tag
from django.http import HttpResponse, HttpResponseRedirect
from .forms import DisplayForm
from django.views.generic import ListView, DetailView


# def index(request):

#     questions = models.Question.objects.filter(status='published')


#     context = {'questions':questions}

#     return render(request, 'questions/index.html', context)


class IndexView(ListView):
     model = Question
     template_name = 'questions/index.html'

    #  def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get the context
    #     context = super(IndexView, self).get_context_data(**kwargs)
    #     # Create any data and add it to the context
    #     # context['some_data'] = 'This is just some data'
    #     return context
    



def ask_question(request):

    if request.method == "POST":
        form = DisplayForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("../")

    else:
        form = DisplayForm()    

    return render(request, 'questions/ask.html', {'form':form})    

    # if request.method == "POST":
    #     form = DisplayForm(request.POST)
    #     if form.is_valid():
    #        post = form.save()
    #        post.author = request.user
    #        post.save()
    #        return redirect("../")


        #     post = form.save(commit=False)
        #     post.author = request.user
        #     post.published_date = timezone.now()
        #     post.save()
        #     return redirect('questions/index.html', pk=post.pk)
    # else:
    #     form = DisplayForm()
    # return render(request, 'questions/ask.html', {'form':form})    


def question_detail(request, q_id):

    question = Question.objects.get(id=q_id)
    answers = question.answer_set.all() #answer_set is the related name for the questions_id foreign key in Answer table

    context = {
        'question':question,
        'answers':answers,
    }

    return render(request, 'questions/question_detail.html', context)


# class QuestionDetailView(DetailView):
#     template_name = 'questions/question_detail.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["answers"] =  
#         return context
    
    



def about_us(request):
    return HttpResponse("this is about us")

def contact(request):
    return HttpResponse("contact page") 
           