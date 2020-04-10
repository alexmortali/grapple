from django.shortcuts import render, reverse, redirect
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.contrib import messages
from .forms import ReviewForm
from .models import Review
from django.contrib.auth.decorators import login_required

User = get_user_model()

# Create your views here.
@login_required()
def add_review(request):
    """ View for a use to add review """

    template = 'add_review.html'
    review_form = ReviewForm()
    context = {'review_form': review_form}

    if request.method == "GET":
        return render(request, template, context)
    elif request.method == "POST":
        user_review_form = ReviewForm(request.POST)

        if user_review_form.is_valid():
            review = user_review_form.save(commit=False)
            review.review_date = timezone.now()
            review.user = request.user
            review.rating = float(review.rating)
            review.save()
        
            messages.success(request, "Review Added")
            #return redirect(reverse('products:list_of_products'))
        else:
            messages.error(request, user_review_form.errors)
    return render(request, template, context)