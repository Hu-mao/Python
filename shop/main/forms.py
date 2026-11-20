from django import forms
from .models import Card


class CardForm(forms.ModelForm):
    title = forms.CharField(
        label="Назва картки",
        min_length=3,
        max_length=100,
        error_messages={
            'required': 'Введіть назву картки.',
            'min_length': 'Назва повинна містити мінімум 3 символи.',
            'max_length': 'Назва не може бути довшою за 100 символів.',
        },
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введіть назву'
        })
    )

    description = forms.CharField(
        label="Опис",
        min_length=10,
        max_length=500,
        error_messages={
            'required': 'Введіть опис картки.',
            'min_length': 'Опис повинен містити мінімум 10 символів.',
            'max_length': 'Опис не може бути довшим за 500 символів.',
        },
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 4,
            'placeholder': 'Введіть опис картки'
        })
    )

    tags = forms.ModelMultipleChoiceField(
        queryset=None,
        required=False,
        label="Теги",
        error_messages={
            'invalid_choice': 'Вибрано неправильний тег.',
        },
        widget=forms.SelectMultiple(attrs={
            'class': 'form-select',
        })
    )

    class Meta:
        model = Card
        fields = ['title', 'description', 'tags']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        from .models import Tag
        self.fields['tags'].queryset = Tag.objects.all()

    def clean_title(self):
        title = self.cleaned_data['title'].strip()

        if not title:
            raise forms.ValidationError("Назва не може бути порожньою.")

        if len(title) < 3:
            raise forms.ValidationError(
                "Назва картки повинна містити хоча б 3 символи."
            )

        return title

    def clean_description(self):
        description = self.cleaned_data['description'].strip()

        if not description:
            raise forms.ValidationError("Опис не може бути порожнім.")

        if len(description) < 10:
            raise forms.ValidationError(
                "Опис занадто короткий. Введіть мінімум 10 символів."
            )

        return description

    def clean_tags(self):
        tags = self.cleaned_data.get('tags')

        if tags and tags.count() > 5:
            raise forms.ValidationError(
                "Можна вибрати не більше 5 тегів."
            )

        return tags