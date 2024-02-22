from django import forms
from .models import Post

class PostForm(forms.ModelForm) : #폼의 이름

    class Meta : #이 폼을 만들기 위해 어떤 모델이 쓰여야 하는지 장고에게 알려주는 구문임. 
        model = Post
        fields= ( 'title' ,'text' )