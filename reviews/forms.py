from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    rating = forms.FloatField(min_value=1, max_value=5, widget=forms.Select(
        choices=[(i, i) for i in range(1, 6)]))
    title = forms.CharField(max_length=35)
    review = forms.CharField(max_length=600, widget=forms.Textarea)

    class Meta:
        model = Review
        fields = ('product', 'title', 'review', 'rating')

    def clean_rating(self, *args, **kwargs):
        rating = self.cleaned_data.get('rating')
        if rating > 5.0 or rating < 1:
            raise forms.ValidationError(
                "Please give a rating between 1 and 5.")
        else:
            return rating

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        if len(title) > 35:
            raise forms.ValidationError(
                "Please use 35 or less characters for title")
        else:
            return title

    def clean_review(self, *args, **kwargs):
        review = self.cleaned_data.get('review')
        if len(review) > 750:
            raise forms.ValidationError(
                "Please use 600 or less characters for review")
        else:
            return review
