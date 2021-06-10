from django.shortcuts import render, redirect
from .forms import UrlForm
from .models import ShortUrls
from .shortener import Shortener


def home(request, token):
    long_url = ShortUrls.objects.filter(short_url=token)[0]
    return redirect(long_url.long_url)


def make(request):
    form = UrlForm(request.POST)
    a = ''
    if request.method == 'POST':
        if form.is_valid():
            new_url = form.save(commit=False)
            a = Shortener().issue_token()
            new_url.short_url = a
            new_url.save()
        else:
            form = UrlForm()
            a = "Invalid Input"
    return render(request, 'home.html', {'form': form, 'a': a})
