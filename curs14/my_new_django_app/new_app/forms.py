from django.forms import ModelForm, ValidationError
from .models import BlogPost

class BlogPostForm(ModelForm):
    class Meta:
        fields = ('title', 'content', 'author')
        model = BlogPost

    def clean_title(self):
        if 'web' in self.cleaned_data['title']:
            raise ValidationError('Web article cannot be added')
        return self.cleaned_data['title']