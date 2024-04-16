from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('customer_name','project_title','contract','overview','period','current_process','status_status','situation_details','person','contact_information','unit_price','business_trip','one_word_appeal',)