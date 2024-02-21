from django.shortcuts import render, redirect
from django.views import View
from ..forms import UserRegistrationForm

class RegisterView(View):
    def get(self, request):
        form = UserRegistrationForm()
        return render(request, 'general/user_form.html', {'form': form})

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('top')  # 登録成功後のリダイレクト先を指定
        return render(request, 'general/user_form.html', {'form': form})