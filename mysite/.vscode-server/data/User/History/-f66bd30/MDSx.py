from django.shortcuts import render, redirect
from ..forms import UserRegisterForm

def user_register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')  # 登録成功後のリダイレクト先を設定してください
    else:
        form = UserRegisterForm()
    return render(request, 'user_register.html', {'form': form})
