from django.contrib import admin
from .models import User, Card, Tag

admin.site.register(User)
admin.site.register(Card)
admin.site.register(Tag)