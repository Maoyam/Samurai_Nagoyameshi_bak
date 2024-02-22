from django.shortcuts import render, redirect, get_object_or_404
from general.forms import ReviewForm
from commondb.models.restaurant import Restaurant
from commondb.models.review import Review
from django.http import JsonResponse

def submit_review(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.name = restaurant
            review.save()
            return redirect('general/shop_detail/<restaurant_id>/', review_id=review.id)
    else:
        form = ReviewForm()
    return render(request, 'general/submit_review/<int:restaurant_id>/', {'form': form, 'restaurant': restaurant})
