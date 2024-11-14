import random
import string
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import URL
from .forms import URLForm

def generate_short_url():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

def index(request):
    form = URLForm()
    shortened_url = None

    if request.method == "POST":
        form = URLForm(request.POST)
        if form.is_valid():
            original_url = form.cleaned_data['original_url']
            
            # Check if the original URL already exists
            existing_url = URL.objects.filter(original_url=original_url).first()
            if existing_url:
                shortened_url = existing_url.shortened_url
            else:
                # Generate a unique short URL
                shortened_url = generate_short_url()
                while URL.objects.filter(shortened_url=shortened_url).exists():
                    shortened_url = generate_short_url()

                # Save the URL mapping
                new_url = URL(original_url=original_url, shortened_url=shortened_url)
                new_url.save()

    return render(request, 'shortner/index.html', {'form': form, 'shortened_url': shortened_url})

def redirect_url(request, shortened_url):
    url = get_object_or_404(URL, shortened_url=shortened_url)
    return redirect(url.original_url)
