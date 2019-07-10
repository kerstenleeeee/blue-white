from django import forms
import re
import base64
from . import models

class DocumentForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(DocumentForm, self).__init__(*args, **kwargs)
		self.fields['document'].label = ""

	class Meta:
		model = models.Files
		fields = ('document',)