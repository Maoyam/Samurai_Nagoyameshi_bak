from django import forms
from commondb.models.review import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['restaurant', 'visit_date', 'rating', 'images', 'comment']
        widgets = {
            'visit_date': forms.DateInput(attrs={'type': 'date'}),
            'rating': forms.Select(choices=[(i, str(i)) for i in range(1, 6)], attrs={'class': 'rating'}),
            'images': forms.ClearableFileInput(attrs={'multiple': True}),
        }
      