from django import forms

from post.models import Post, Tag, Comment


class TagForm(forms.Form):
    name = forms.CharField(max_length=255, label='Tag name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    # slug = forms.CharField(max_length=255, label='Slug (will be created automatically)',
    #                        widget=forms.TextInput(attrs={'class': 'form-control'}))


class PostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['content'].widget.attrs.update({'class': 'form-control'})
        # self.fields['tags'].widget.attrs.update({'class': 'form-control'})

    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Post
        fields = '__all__'


class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['comment_field'].widget.attrs.update({
            'class': 'form-control',
            'style': 'resize: none; width: 100%; padding: 10px; box-sizing: border-box; border-color: #375A7F;'
                     'background-color: #303030; color: white;',
        })

    class Meta:
        model = Comment
        fields = ('comment_field',)


class ReplyForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['comment_field'].widget.attrs.update({
            'class': 'form-control',
        })

    class Meta:
        model = Comment
        fields = ('comment_field',)
