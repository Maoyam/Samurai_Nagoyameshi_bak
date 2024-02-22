from django.shortcuts import render, redirect, get_object_or_404
from general.forms import ReviewForm
from commondb.models.restaurant import Restaurant
from commondb.models.review import Review
from django.http import HttpResponse

def submit_review(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.name = restaurant
            review.save()
            return redirect('review_confirmation')
    else:
        form = ReviewForm()
    return render(request, 'general/submit_review.html', {'form': form, 'restaurant': restaurant})

# 送信後の完了画面
def review_confirmation(request):
    restaurant_id = request.session.get('restaurant_id')  # レビュー投稿で設定されたrestaurant_idをセッションから取得
    if not restaurant_id:
        # もしrestaurant_idがセッションにない場合は、適切なエラー処理を行うか、リダイレクトするなどの方法で対処する
        return HttpResponse("Error: restaurant_id is missing")
    return render(request, 'general/review_confirmation.html', {'restaurant_id': restaurant_id})