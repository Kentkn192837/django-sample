# 自分で新しく追加したファイル
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),    # views.pyのindex関数が実行される
    path('<int:id>/<nickname>/', views.show, name='show'),
    path('my_name_is_<nickname>.I_am_<int:age>_years_old.', views.another_pattern, name='another_pattern')
]
