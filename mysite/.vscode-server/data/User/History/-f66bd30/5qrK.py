from django.views.generic.edit import CreateView
from commondb.models.user import User
 
class UserRegisterView(CreateView):
    model = User
    
    fields = ['username', 'email', 'password', 'password2']
   
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True
 