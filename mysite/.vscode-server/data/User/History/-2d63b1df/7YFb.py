from django import forms
from commondb.models.review import Review

class ReviewForm(forms.ModelForm):    
    class Meta:
        model = Review
        fields = ['訪問日', '評価', '感想', '画像', '画像', '画像']
        widgets = {
            'visit_date': forms.DateInput(attrs={'class': 'form-control'}),
            'rating': forms.Select(attrs={'class': 'form-select'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'image1': forms.FileInput(attrs={'class': 'form-control'}),
            'image2': forms.FileInput(attrs={'class': 'form-control'}),
            'image3': forms.FileInput(attrs={'class': 'form-control'}),
        }
      