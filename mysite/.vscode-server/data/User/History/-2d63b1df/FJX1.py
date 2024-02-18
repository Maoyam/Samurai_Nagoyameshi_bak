from django import forms
from commondb.models.review import Review
from commondb.models.user import User

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
            'visit_date': forms.DateInput(attrs={'class': 'form-control',"type": "date"}),
            'rating': forms.Select(attrs={'class': 'form-select'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'image1': forms.FileInput(attrs={'class': 'form-control'}),
            'image2': forms.FileInput(attrs={'class': 'form-control'}),
            'image3': forms.FileInput(attrs={'class': 'form-control'}),
        }
             
        
class UserRegisterForm(forms.ModelForm):
    # 新規ユーザー登録用フォーム
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')  # password2をfieldsに追加
        widgets = {
            'username': forms.CharField(attrs={'class': 'form-control', 'placeholder': 'ユーザー名'}),
            'email': forms.EmailField(attrs={'class': 'form-control', 'placeholder': 'メールアドレス'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'パスワード'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '確認用パスワード'})
        }
        
    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput()
    )
            
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True