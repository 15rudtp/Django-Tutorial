from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.post_list, name = 'post_list'),
    path('post/<int:pk>/',views.post_detail, name = "post_detail"),
    path('post/new',views.post_new, name = "post_new"),
    # path('post-data/<int:pk>/',views.post_data, name = "post_data"),
    # <int : id > 여기 서 id는 views.py 파일의 랜더함수로 전달된다.
    # 랜더함수의 두 번째 파라미터로 받는다.
]
