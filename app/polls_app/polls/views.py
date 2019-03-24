from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, Http404
# from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone
# Create your views here.

from .forms import PollsDetailForm, PollsVoteForm
from .models import Choice, Question

from django.db.models import Avg, Max, Min


class IndexView(generic.ListView):
    model = Question
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class PollsDetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    form_class = PollsDetailForm

    # questionにQuestionの結果が渡される
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        form = self.form_class(self.kwargs)
        if form.is_valid():
            value = list(form.data.values())[0]

            # questions = Question.objects.filter(
            #     pk=value,
            #     pub_date__lte=timezone.now()
            # )

            # if not questions:
            #     raise Http404("Question does not exist")

            try:
                Question.objects.get(
                    pk=value,
                    pub_date__lte=timezone.now()
                )
            except Question.DoesNotExist:
                raise Http404("Question does not exist")

        return Question.objects.filter(pub_date__lte=timezone.now())

    def post(self, request, *args, **kwargs):
        detail_form = PollsDetailForm(kwargs)

        if detail_form.is_valid():
            vote_form = PollsVoteForm(request.POST)
            question = get_object_or_404(Question, pk=kwargs['pk'])

            if vote_form.is_valid():
                try:
                    selected_choice = question.choice_set.get(
                        pk=request.POST['choice']
                    )
                except (KeyError, Choice.DoesNotExist):
                    # request.POST['choice'] は KeyError を送出
                    return render(request, 'polls/detail.html', {
                        'question': question,
                        'error_message': "You didn't select a choice.",
                    })
                else:
                    selected_choice.votes += 1
                    selected_choice.save()

                    return HttpResponseRedirect(
                        reverse('polls:results', args=(question.id,))
                    )
            else:
                error_message = "choice is not in the correct format."
                return render(
                    request,
                    'polls/detail.html', {
                        'question': question,
                        'error_message': error_message
                    }
                )
        else:
            raise Http404("Question does not exist")


class PollsResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
    form_class = PollsDetailForm

    def get_context_data(self, **kwargs):
        context = super(PollsResultsView, self).get_context_data(**kwargs)

        form = self.form_class(self.kwargs)
        if form.is_valid():
            try:
                # questions
                questions = get_object_or_404(
                    Question,
                    pk=self.kwargs['pk'],
                    pub_date__lte=timezone.now()
                )
                context['question'] = questions

                # max, min, avg
                context['max'] = Choice.objects.aggregate(
                    Max('votes')
                )['votes__max']
                context['min'] = Choice.objects.aggregate(
                    Min('votes')
                )['votes__min']
                context['avg'] = Choice.objects.aggregate(
                    Avg('votes')
                )['votes__avg']
            except Question.DoesNotExist as e:
                # raise Http404(e)
                raise Exception(e)

        return context


# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)

#     try:
#         form = PollsVoteForm(request.POST)
#         print(form.is_valid())
#         selected_choice = question.choice_set.get(
#             pk=request.POST['choice']
#         )
#         print(request.POST)
#         print(selected_choice)
#     except (KeyError, Choice.DoesNotExist):
#         # request.POST['choice'] は KeyError を送出
#         return render(request, 'polls/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()

#         return HttpResponseRedirect(
#             reverse('polls:results', args=(question.id,))
#         )
