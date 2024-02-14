from django import forms
from commondb.models.review import Review, ReviewImage

class ReviewForm(forms.ModelForm):
    class Meta:
      model = Review
      fields = ['restaurant', 'visit_date', 'rating', 'comment']
      
class ReviewImageForm(forms.ModelForm):
    class Meta:
      model = ReviewImage
      fields = ['image']