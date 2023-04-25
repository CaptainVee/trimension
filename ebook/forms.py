from django import forms
from django.utils.translation import gettext_lazy as _
from ebook.models import Book, Page


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            "title",
            "description",
        ]
        labels = {
            "title": _("Book Title"),
            "description": _(" "),
        }

class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = [
            "text",
            "image",
            "model",
        ]