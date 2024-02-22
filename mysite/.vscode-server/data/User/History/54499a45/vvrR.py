from django.shortcuts import render, redirect, get_object_or_404
from general.forms import ReviewForm
from commondb.models.restaurant import Restaurant
from commondb.models.review import Review

def submit_review(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.name = restaurant
            review.save()
            return redirect('review_confirmation', restaurant_id=restaurant_id)
    else:
        form = ReviewForm()
    return render(request, 'general/submit_review.html', {'form': form, 'restaurant': restaurant})

# 送信後の完了画面
def review_confirmation(request):
    return render(request, 'general/review_confirmation.html')

