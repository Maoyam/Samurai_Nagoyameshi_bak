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
            # visit_dateを文字列に変換
            review.visit_date = review.visit_date.isoformat()
            review.save()
            # JSONレスポンスを返す場合、visit_dateは文字列に変換されます
            return redirect('review_confirm', review_id=review.id)
    else:
        form = ReviewForm()
    return render(request, 'general/submit_review.html', {'form': form, 'restaurant': restaurant})
