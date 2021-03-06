from member.forms import SignupModelForm
from django.shortcuts import render, redirect
from django.contrib.auth import login


def signup(request):
    context = {}
    if request.method == 'POST':
        form = SignupModelForm(request.POST)
        if form.is_valid():
            user = form.save()

            login(request, user)
            return redirect('video:category_list')
        context['form'] = form
    else:
        form = SignupModelForm()
        context['form'] = form
    return render(request, 'member/signup.html', context)


