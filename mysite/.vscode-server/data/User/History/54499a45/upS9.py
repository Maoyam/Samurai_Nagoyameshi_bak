from django.shortcuts import render, redirect, get_object_or_404
from general.forms import ReviewForm
from commondb.models.restaurant import Restaurant

def submit_review(request, restaurant_id):
    restaurant = get_object_or_404(pk=restaurant_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            request.session['review_data'] = form.cleaned_data
            return redirect('shop_detail', pk=restaurant_id)
    else:
        form = ReviewForm()
    return render(request, 'general/submit_review.html', {'form': form, 'restaurant': restaurant})


def review_confirm(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    review_data = request.session.get('review_data')  # セッションからフォームデータを取得
    if review_data:
        review_form = ReviewForm(initial=review_data)
    else:
        return redirect('submit_review', restaurant_id=restaurant_id)
    return render(request, 'general/review_confirm.html', {'review_form': review_form, 'restaurant': restaurant})

