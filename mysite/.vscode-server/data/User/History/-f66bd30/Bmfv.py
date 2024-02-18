from django.views.generic.edit import CreateView
from commondb.models.user import User
 
class UserRegisterView(CreateView):
    model = User
    
    fields = ['username', 'email', 'password', 'password2']
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
 