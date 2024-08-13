from django.shortcuts import render, get_object_or_404, redirect
from .models import Slider, Credit
from .forms import SliderForm, CreditForm

# Slider views
def slider_list(request):
    sliders = Slider.objects.all()
    return render(request, 'slider_list.html', {'sliders': sliders})

def slider_detail(request, pk):
    slider = get_object_or_404(Slider, pk=pk)
    return render(request, 'slider_detail.html', {'slider': slider})

def slider_create(request):
    if request.method == "POST":
        form = SliderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('slider_list')
    else:
        form = SliderForm()
    return render(request, 'slider_form.html', {'form': form})

def slider_update(request, pk):
    slider = get_object_or_404(Slider, pk=pk)
    if request.method == "POST":
        form = SliderForm(request.POST, request.FILES, instance=slider)
        if form.is_valid():
            form.save()
            return redirect('slider_list')
    else:
        form = SliderForm(instance=slider)
    return render(request, 'slider_form.html', {'form': form})

def slider_delete(request, pk):
    slider = get_object_or_404(Slider, pk=pk)
    if request.method == "POST":
        slider.delete()
        return redirect('slider_list')
    return render(request, 'slider_confirm_delete.html', {'slider': slider})

# Credit views
def credit_list(request):
    credits = Credit.objects.all()
    return render(request, 'credit_list.html', {'credits': credits})

def credit_create(request):
    if request.method == "POST":
        form = CreditForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('credit_list')
    else:
        form = CreditForm()
    return render(request, 'credit_form.html', {'form': form})

def credit_update(request, pk):
    credit = get_object_or_404(Credit, pk=pk)
    if request.method == "POST":
        form = CreditForm(request.POST, instance=credit)
        if form.is_valid():
            form.save()
            return redirect('credit_list')
    else:
        form = CreditForm(instance=credit)
    return render(request, 'credit_form.html', {'form': form})

def credit_delete(request, pk):
    credit = get_object_or_404(Credit, pk=pk)
    if request.method == "POST":
        credit.delete()
        return redirect('credit_list')
    return render(request, 'credit_confirm_delete.html', {'credit': credit})
