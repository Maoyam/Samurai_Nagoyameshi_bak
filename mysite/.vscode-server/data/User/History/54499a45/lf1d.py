from django.shortcuts import render, redirect
from commondb.models.restaurant import Restaurant
from commondb.models.review import Review
from commondb.models.restaurant import Restaurant

def submit_review(request):
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        image_forms = [ReviewImageForm(request.POST, request.FILES, prefix=str(x)) for x in range(3)]
        if review_form.is_valid() and all(image_form.is_valid() for image_form in image_forms):
            review = review_form.save()
            for image_form in image_forms:
                if 'image' in image_form.cleaned_data:
