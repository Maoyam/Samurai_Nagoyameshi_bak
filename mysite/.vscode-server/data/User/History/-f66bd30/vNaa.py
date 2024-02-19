from django.shortcuts import render, redirect
from ..forms import UserRegisterForm

class UserRegisterView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'user_register.html', {'form': form})

    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('general/top/')  # 登録成功後のリダイレクト先を設定してください
        return render(request, 'user_register.html', {'form': form})
