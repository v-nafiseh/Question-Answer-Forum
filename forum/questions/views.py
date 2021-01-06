from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.utils import timezone
from .models import Question, Answer, Tag
from django.http import HttpResponse, HttpResponseRedirect
from .forms import DisplayForm, NewCommentForm
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView, RedirectView
from django.contrib.auth import authenticate, login
from django.urls import reverse
from .forms import NewCommentForm
from django.views.generic.edit import FormMixin, ModelFormMixin



class IndexView(ListView):
     template_name = 'questions/index.html'
     context_object_name = 'questions'

     def get_queryset(self):
         return Question.objects.all()


class AskView(CreateView):
    template_name = 'questions/ask.html'
    queryset = Question.objects.all()
    form_class = DisplayForm
    # model = Question
    def get_success_url(self):
        return reverse('questions:id', kwargs={'id':self.object.id})



class QuestionDetailView(FormMixin, DetailView):
    template_name = 'questions/question_detail.html'
    context_object_name = 'question'
    form_class = NewCommentForm
    
    def get_object(self):
        id_=self.kwargs.get("id")
        return get_object_or_404(Question, id=id_)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        answers = self.get_object().answer_set.all()
        # context["form"] = NewCommentForm(initial={'id':self.object})
        context["form"] = self.get_form()
        context["answers"] = answers
        return context

    def get_success_url(self):
        return reverse('questions:detail', kwargs={'question_id':self.object.id}) 

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            form.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    # def form_valid(self, form):
    #     form.save()
    #     return super(ParticularPost, self).form_valid(form)        









    # def create_answer(self, request, *args, **kwargs):
    #     new_answer = Answer(content=request.POST.get('content'),
    #                         author=self.request.user,
    #                         question_id=self.get_object())   
    #     new_answer.save() 

    #     return self.get(self, request, *args, **kwargs)    

    # def get_success_url(self):
    #     return reverse('questions:id', kwargs={'id':self.object.id})                      



class AnswerView(CreateView):
    pass        

class TagView(CreateView):
    pass


class LikeView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        id_ = self.kwargs.get('id')
        obj = get_object_or_404(Question, id=id_)
        user = self.request.user
        url = obj.get_absolute_url()
        if user.is_authenticated:
            if user in obj.likes.all():
                obj.likes.remove(user)
            else:
                obj.likes.add(user) 
        return url 


# class AnswerLikeView(RedirectView):
#     def get_redirect_url(self, *args, **kwargs):
#         id_ = self.kwargs.get('id')
#         obj = get_object_or_404(Question, id=id_)
#         user = self.request.user
#         url = obj.get_absolute_url()
#         if user.is_authenticated:
#             if user in obj.likes.all():
#                 obj.likes.remove(user)
#             else:
#                 obj.likes.add(user) 
#         return url 
        


class AnswerView(CreateView):
    # template_name = 'questions/question_detail.html'
    pass

class EditQuestion(UpdateView):
    pass

class DeleteQuestion(DetailView):
    pass
        

class EditAnswer(UpdateView):
    pass

class DeleteAnswer(DeleteView):
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
