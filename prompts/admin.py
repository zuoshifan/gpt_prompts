from django.contrib import admin
from .models import Category, PromptType, Prompt#, Purchase

# # Register your models here.
# Register Category model with default options
admin.site.register(Category)

# Register PromptType model with default options
admin.site.register(PromptType)

# Register Prompt model with default options
admin.site.register(Prompt)

# # Register Purchase model with default options
# admin.site.register(Purchase)
