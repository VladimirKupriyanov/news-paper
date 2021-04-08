from django.forms import ModelForm
from .models import Post


# Создаём модельную форму
class PostForm(ModelForm):
    # в класс мета как обычно надо написать модель по которой будет строится форма и нужные нам поля.
    class Meta:
        model = Post
        fields = ['title', 'text', 'author', 'categoryType', 'postCategory']
