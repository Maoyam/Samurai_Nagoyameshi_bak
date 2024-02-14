from django import forms
from commondb.models.review import Review

class DateInput(forms.DateInput):
    input_type = 'date'

class ReviewForm(forms.ModelForm):
    
    class Meta:
        model = Review
        fields = ['visit_date', 'rating', 'comment', 'image1', 'image2', 'image3']
        labels = {
            'name': '店名',
            'visit_date': '訪問日',
            'rating': '評価',
            'comment': 'コメント',
            'image1': '画像',
            'image2': '画像',
            'image3': '画像',
        }
        widgets = {
            'visit_date': forms.DateInput(attrs={'class': 'form-control'}),DateInput(),
            'rating': forms.Select(attrs={'class': 'form-select'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'image1': forms.FileInput(attrs={'class': 'form-control'}),
            'image2': forms.FileInput(attrs={'class': 'form-control'}),
            'image3': forms.FileInput(attrs={'class': 'form-control'}),
        }
      