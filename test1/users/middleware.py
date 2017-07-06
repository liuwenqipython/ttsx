import views
from django.shortcuts import render,redirect

class TestMeddleware():
    def process_view(request, view_func, view_args, view_kwargs):
        if request.session['islogin']!=True:
            return redirect('/login/')
