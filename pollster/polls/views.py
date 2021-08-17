from django.shortcuts import render,redirect
from .models import Question, Choice
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.template import loader
from django.urls import reverse
from .forms import CreateQuestion

# Create your views here.


def createQue(request):
    if request.method == 'POST':
        form = CreateQuestion(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.save()
            new_choice1 = Choice(question=question,
                                 choice_text=form.cleaned_data['choice1']).save()
            new_choice2 = Choice(question=question,
                                 choice_text=form.cleaned_data['choice2']).save()
            new_choice3 = Choice(question=question,
                                 choice_text=form.cleaned_data['choice3']).save()
            new_choice4 = Choice(question=question,
                                 choice_text=form.cleaned_data['choice4']).save()
            return redirect('index')
    else:
        form = CreateQuestion(request.POST)
    context = {'form': form}
    return render(request, 'polls/create.html', context)


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404('Question does not exist')
    context = {'question': question}
    return render(request, 'polls/detail.html', context)


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'polls/results.html', context)


def vote(request, question_id):
    question = Question.objects.get(pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'question': question, 'error_message': "You didn't select a choice"},)
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
