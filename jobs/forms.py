from django import forms

from accounts.models import Profession
from .models import JobPost

class JobPostForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Profession.objects.all())

    class Meta:
        model = JobPost
        fields = ['title', 'category', 'description']
        help_texts = {'description': "Enter as much detail about the job as possible",
                      'category': "Select the profession that the job falls under",
                      'title': 'Enter title for the job'
                      }


    def __init__(self, *args, **kwargs):
        super(JobPostForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            help_text = self.fields[field].help_text
            self.fields[field].help_text = None
            if help_text != '':
                self.fields[field].widget.attrs.update(
                    {'class': 'has-popover', 'data-content': help_text, 'data-placement': 'left',
                     'data-container': 'body'})