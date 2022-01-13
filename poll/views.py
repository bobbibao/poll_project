from django.views import View
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import CreatePollForm
from .models import Poll
from django.contrib.auth import authenticate, login, decorators, logout
from django.contrib.auth.mixins import LoginRequiredMixin

@decorators.login_required(login_url='/login/')
def home(request):
    polls = Poll.objects.all()

    context = {
        'polls' : polls
    }
    return render(request, 'poll/home.html', context)

def create(request):
    if request.method == 'POST':
        form = CreatePollForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('home')
    else:
        form = CreatePollForm()

    context = {'form' : form}
    return render(request, 'poll/create.html', context)

def results(request):
    poll = Poll.objects.all()
    context = {
        'poll': poll,
    }
    if request.user.has_perm('Login.view_post'):
        return render(request, 'poll/results.html', context)
    return redirect('home')

def view_one_question(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)

    context = {
        'poll' : poll
    }
    return render(request, 'poll/view-one-question.html', context)

def vote(request, poll_id):
    try:
        poll = Poll.objects.get(pk=poll_id)

        if request.method == 'POST':

            selected_option = request.POST['poll']
            if selected_option == 'option1':
                poll.option_one_count += 1
            elif selected_option == 'option2':
                poll.option_two_count += 1
            elif selected_option == 'option3':
                poll.option_three_count += 1
            else:
                return HttpResponse(400,'Invalid form option')
            poll.save()
            return redirect('home')
    except:
        return HttpResponse(400,'Invalid form option')

    context = {
        'poll' : poll
    }
    return render(request, 'poll/vote.html', context)
class Login( View):
    def get(self, request):
        return render(request, 'poll/login.html')
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        users = authenticate(username= username, password= password)
        if users is None:
             return render(request, 'poll/login.html')
        login(request, users)
        return redirect('home')

class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('login')
def delete(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    poll.delete()
    return redirect('home')