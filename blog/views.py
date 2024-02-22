from django.http import JsonResponse,HttpResponse #데이터를 response할 때
from django.shortcuts import render, get_object_or_404 #render : 랜더링 , get_object_or_404 : 찾을 수 없을 때
from django.shortcuts import redirect
from django.utils import timezone
from .models import Post # .은 같은 경로에 있는 파일일 때 붙힌다. 
from .forms import PostForm
# Create your views here.


#게시글 전체 조회
def post_list(request) : 
    posts = Post.objects.order_by('published_date') #정렬 쿼리셋을 이용한 데이터 조회
    return render ( request , 'blog/post_list.html' , { 'posts' : posts })

#게시글 디테일
def post_detail(request, pk) : #request는 해당 url페이지에서 입력한 데이터가 들어가 있다.
    post = get_object_or_404(Post, pk = pk)
    return render ( request , 'blog/post_detail.html' , { 'post' : post })

#게시글 작성
def post_new(request) : 
    if request.method == "POST" :
        form = PostForm(request.POST) 
        if form.is_valid() : #필드 값 유효성 검사
            post = form.save(commit=False) #commit=False : 넘겨진 데이터를 바로 POST 모델에 저장하지 말라는 뜻.
            post.author = request.user
            post.published_date=timezone.now()
            post.save()
        return redirect('post_detail', pk = post.pk)
    else : 
        form = PostForm()
    
    return render (request, 'blog/post_edit.html', {'form' : form})

# def post_data(request, pk) : 
#     post = get_object_or_404(Post,pk = pk)
#     data = {
#         'id' : post.pk,
#         'title' : post.title,
#     }
#     return HttpResponse(data)