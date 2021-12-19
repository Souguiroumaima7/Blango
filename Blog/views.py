from django.shortcuts import render

# Create your views here.
from django.template.defaulttags import comment
from django.utils import timezone
import blog.models
from django.shortcuts import render , get_object_or_404
from crispy_forms.layout import Submit
from crispy_forms.helper import FormHelper

from Blog import forms


def index(request) :
    posts = Post.objects.filter(published_at__lte=timezone.now())
    return render(request , "blog/index.html" , {"posts" : posts})

    def post_detail(request , slug , post=None) :
        post = get_object_or_404(post , slug=slug)
        return render(request , "blog/post_detail.html" , {"post:post"})

    if request.user is active :
        if request.method == "POST" :
            comment_form = commentForm(request.POST)

            if comment_form.is_valid() :
                comment = comment_form.save(commit=False)
                comment.content_object = post
                comment.creator = request.user
                comment.save()
                return render(
                    request , "blog/post-detail.html" , {"post" : post , "comment_form" : comment_form}
                )

        else :
            comment_form = commentForm()




class commentForm(forms.ModelForm) :
    class Meta :
        model = comment
        fields = ["contenttent"]

    def _init_(self , *args , **kwargs) :
        super(commentForm , self)._init_(*args , **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(submit('submit' , 'submit'))
