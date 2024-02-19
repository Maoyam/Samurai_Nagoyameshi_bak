from django.views.generic.edit import CreateView
from commondb.models.user import User
 
class UserRegisterView(CreateView):
    model = User
    
    fields = ['username', 'email', 'password']
   
 