from django.shortcuts import render, redirect
from general.forms import ReviewForm
from commondb.models.restaurant import Restaurant

def submit_review(request, restaurant_id):
    restaurant = Restaurant.objects.get(id=restaurant_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.restaurant_id = restaurant.id
            review.save()
            return redirect('shop_detail', restaurant_id=restaurant_id)
    else:
        form = ReviewForm()
    return render(request, 'general/submit_review.html', {'form': form})