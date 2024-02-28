from django.http import JsonResponse,HttpResponse #데이터를 response할 때
from django.shortcuts import render, get_object_or_404 #render : 랜더링 , get_object_or_404 : 찾을 수 없을 때
from django.shortcuts import redirect
from django.utils import timezone
from .models import Post # .은 같은 경로에 있는 파일일 때 붙힌다. 
from .forms import PostForm
# Create your views here.


#게시글 전체 조회
def post_list(request) : 
    posts = Post.objects.filter(published_date__isnull = False).order_by('published_date') #정렬 쿼리셋을 이용한 데이터 조회
    return render ( request , 'blog/post_list.html' , { 'posts' : posts })

#게시글 디테일 (게시글 조회)
def post_detail(request, pk) : #request는 해당 url페이지에서 입력한 데이터가 들어가 있다.
    post = get_object_or_404(Post, pk = pk) #데이터를 GET하거나 404에러 반환
    return render ( request , 'blog/post_detail.html' , { 'post' : post })

#게시글 작성 (게시글 생성)
def post_new(request) : 
    if request.method == "POST" :
        form = PostForm(request.POST) 
        if form.is_valid() : #필드 값 유효성 검사
            post = form.save(commit=False) #commit=False : 넘겨진 데이터를 바로 POST 모델에 저장하지 말라는 뜻.
            post.author = request.user #request에는 user 정보가 자동으로 담겨서 오는 듯
            #post.published_date=timezone.now()
            post.save()
        return redirect('post_detail',pk = post.pk) #urls 의 name이 뭔가 했더니 리다이렉트 할 때 사용되는 거 같다.
    else : 
        form = PostForm()
    
    return render (request, 'blog/post_edit.html', {'form' : form})


#게시글 수정
def post_edit(request,pk) : # 1. url로부터 매개변수 pk 받음
    post = get_object_or_404(Post,pk = pk) # 2. 매개변수 pk로 데이터 조회 함
    if request.method == "POST" : # 3. 요청 데이터의 메소드가 POST
        form = PostForm(request.POST, instance=post) # 4. 아마도 form이라는 변수 안에 내가 작성한 내용들이 들어가 있는듯.
        if form.is_valid() :
            post = form.save(commit = False) # 5. form에서 가져온 데이터로 기존 데이터를 수정한다. commit = False는 save함수 사용하면서 저장하지 말라는 뜻.
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk = post.pk)
    else :
        form = PostForm(instance=post)
        return render(request, 'blog/post_edit.html', { 'form' : form })
    
#게시글 삭제
def post_delete(request,pk) :
    post = get_object_or_404(Post,pk = pk)
    if request.method == "POST"  :
        post.delete()
        return redirect("post_list")
    else :
        return redirect("post_detail", pk = post.pk)

#게시글 미리보기
def post_draft_list(request) :
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date') #쿼리셋 기억하기
    return render(request, 'blog/post_draft_list.html', { 'posts': posts })

#게시글 발행하기
def post_publish(request, pk) : 
    post = get_object_or_404(Post,pk = pk)
    post.publish()
    return redirect('post_detail', pk = pk)


#데이터 리스폰스
def post_data(request, pk) : 
    post = get_object_or_404(Post,pk = pk)
    data = {
        'id' : post.pk,
        'title' : post.title,
        'content' : post.text,
    }
    return JsonResponse(data)