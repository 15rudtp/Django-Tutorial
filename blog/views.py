from django.shortcuts import render
from .models import Post # .은 같은 경로에 있는 파일일 때 붙힌다. 

# Create your views here.


def post_list(request) : 
    posts = Post.objects.order_by('published_date') #정렬 쿼리셋을 이용한 데이터 조회
    return render ( request , 'blog/post_list.html' , { 'posts' : posts })