from django.shortcuts import render, redirect

from .forms import BaseForm

def my_view(request):
    if request.method == 'POST':
        form = BaseForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = BaseForm()
    
    return render(request, 'product_reviews/index.html', {'form': form})