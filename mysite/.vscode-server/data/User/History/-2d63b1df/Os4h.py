from django import forms
from commondb.models.review import Review
from commondb.models.user import User
from django.contrib.auth.forms import UserCreationForm
from commondb.models.user import User

class ReviewForm(forms.ModelForm):
    
    class Meta:
        model = Review
        fields = ['visit_date', 'rating', 'comment', 'image1', 'image2', 'image3']
        labels = {
            'user': 'ユーザーID'
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


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='必須。有効なメールアドレスを入力してください。')
    password1 = forms.CharField(widget=forms.PasswordInput, help_text='8文字以上である必要があります。')
    password2 = forms.CharField(widget=forms.PasswordInput, help_text='同じパスワードを入力してください。')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'ユーザーID'
        self.fields['email'].label = 'Email'
        self.fields['password1'].label = 'パスワード'
        self.fields['password2'].label = 'パスワード(確認用)'
             