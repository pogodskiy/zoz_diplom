from django import forms
from post.models import Post, CatPost


class PostForm(forms.ModelForm):
    title = forms.CharField(label='Название')
    post_body = forms.CharField(label='Описание', widget=forms.Textarea)
    comments = forms.CharField(label='Комментарии', required=False)
    cat = forms.ModelChoiceField(label='Категория', queryset=CatPost.objects.all())

    class Meta:
        model = Post
        fields = ('title', 'post_body', 'cat', 'comments')
