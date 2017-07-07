# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from models import Post, Comment

# Create your forms here.
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)
