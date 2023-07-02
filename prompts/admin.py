from django.contrib import admin
from .models import Category, Template, Prompt, Purchase

# Register your models here.
# Register Category model with default options
admin.site.register(Category)

# Register Template model with default options
admin.site.register(Template)

# Register Prompt model with default options
admin.site.register(Prompt)

# Register Purchase model with default options
admin.site.register(Purchase)
