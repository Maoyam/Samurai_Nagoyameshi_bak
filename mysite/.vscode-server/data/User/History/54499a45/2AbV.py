from django.shortcuts import render, redirect, get_object_or_404
from general.forms import ReviewForm
from commondb.models.restaurant import Restaurant
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


def review_confirm(request, review_id, restaurant_id):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    review_data = request.session.get('review_data')  # セッションからレビューデータを取得
    if review_data:
        # セッションから取得したデータを使用してフォームを初期化
        review_form = ReviewForm(initial=review_data)
    else:
        # レビューデータがセッションにない場合は、リダイレクトする
        return redirect('submit_review', restaurant_id=restaurant.id)  # リダイレクト先を指定する
    return render(request, 'general/review_confirm.html', {'review_form': review_form})

