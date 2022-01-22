# 自分で新しく追加したファイル
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),    # views.pyのindex関数が実行される
]
