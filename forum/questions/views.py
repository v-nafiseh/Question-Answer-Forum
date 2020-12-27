from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.utils import timezone
from .models import Question, Answer, Tag
from django.http import HttpResponse, HttpResponseRedirect
from .forms import DisplayForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView




class IndexView(ListView):
     template_name = 'questions/index.html'
     context_object_name = 'questions'

     def get_queryset(self):
         return Question.objects.all()


class AskView(CreateView):
    template_name = 'questions/ask.html'
    queryset = Question.objects.all()
    form_class = DisplayForm


class QuestionDetailView(DetailView):
    template_name = 'questions/question_detail.html'
    context_object_name = 'question'
    
    def get_object(self):
        id_=self.kwargs.get("id")
        return get_object_or_404(Question, id=id_)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        answers = self.get_object().answer_set.all()
        context["answers"] = answers
        return context

class UpdateView(UpdateView):
    pass

class DeleteView(DetailView):
    pass
        


def about_us(request):
    return HttpResponse("this is about us")

def contact(request):
    return HttpResponse("contact page")    


#def index(request):

#   questions = models.Question.objects.filter(status='published')
#   context = {'questions':questions}
#   return render(request, 'questions/index.html', context)

        
# def get_context_data(self, **kwargs):
#     # Call the base implementation first to get the context
#     context = super(IndexView, self).get_context_data(**kwargs)
#     # Create any data and add it to the context
#     # context['some_data'] = 'This is just some data'
#     return context
    


# def ask_question(request):

#     if request.method == "POST":
#         form = DisplayForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("../")

#     else:
#         form = DisplayForm()    

#     return render(request, 'questions/ask.html', {'form':form})    




# def question_detail(request, q_id):

#     question = Question.objects.get(id=q_id)
#     answers = question.answer_set.all() #answer_set is the related name for the questions_id foreign key in Answer table

#     context = {
#         'question':question,
#         'answers':answers,
#     }

#     return render(request, 'questions/question_detail.html', context)

           