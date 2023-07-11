from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
# from markdownx.models import MarkdownxField
from mdeditor.fields import MDTextField

# Create your models here.
# Define a model for prompt categories
class Category(models.Model):
    """
    A model that represents a category of prompts.
    A category has a name that is used to identify and display it.
    A category can have many prompts associated with it.
    """
    # Name field (required, unique, up to 50 characters)
    name = models.CharField(max_length=50, unique=True, verbose_name=_('name'))

    # Slug field (required, unique, up to 50 characters, used for URLs)
    # slug = models.SlugField(max_length=50, unique=True, verbose_name=_('slug'))

    # Meta class for model options
    class Meta:
        # Verbose name and plural name for the model
        verbose_name = _('category')
        verbose_name_plural = _('categories')

        # Ordering option for the model (by name)
        ordering = ('name',)

        # Include all fields in forms and serializers by default
        # fields = '__all__'

    # String representation of the model
    def __str__(self):
        # Return the name of the category
        return self.name

class PromptType(models.Model):
    """
    A model that represents a type of prompt.
    A type has a name that is used to identify and display it.
    A type can have many prompts associated with it.
    """
    # Type field (required, up to 50 characters)
    type = models.CharField(max_length=50, verbose_name=_('type'))

    # Meta class for model options
    class Meta:
        # Verbose name and plural name for the model
        verbose_name = _('Prompt type')
        verbose_name_plural = _('Prompt types')

        # Include all fields in forms and serializers by default
        # fields = '__all__'

    def __str__(self):
        return self.type

# A class for all types of prompts
class Prompt(models.Model):
    """
    A model that represents a prompt.
    A prompt has a title, a category, a cover image, a description, a style, a content, a price in two currencies, a seller, a creation date and time, an update date and time, a feedback, and an approval status.
    A prompt can be viewed, purchased, rated, and commented by users.
    """
    # Title field (required, up to 100 characters)
    title = models.CharField(max_length=100, verbose_name=_('Title'), help_text=_('The title of the prompt.'))

    # Category field (required, many-to-many relation to Category model, related name for reverse lookup)
    category = models.ManyToManyField(Category, related_name='prompt', verbose_name=_('Category'), help_text=_('Categories of the prompt.'))

    # Cover image field (required, image file, stored in covers subdirectory within MEDIA_ROOT)
    cover = models.ImageField(upload_to='covers/', verbose_name=_('Cover image'), help_text=_('A cover image for the prompt.'))

    # Description field (required, up to 500 characters)
    description = models.CharField(max_length=500, verbose_name=_('Description'), help_text=_('Describe what your prompt does to a potential buyer. A more detailed description will increase your sales.'))

    # Conversation style
    STYLE_CHOICES = (
        ('creative', _('More Creative')),
        ('balanced', _('More Balanced')),
        ('precise', _('More Precise')),
    )
    style = models.CharField(max_length=8, choices=STYLE_CHOICES, verbose_name=_('Conversation style'), help_text=_('Choose a conversation style for your prompt.'), default=STYLE_CHOICES[0][0])

    # Content field (required, text field)
    content = models.TextField(verbose_name=_('Content'), help_text=_('Write the content of your prompt.'))

    # Types field (required, many-to-many relation to PromptType model)
    types = models.ManyToManyField(PromptType, verbose_name=_('Prompt types'), help_text=_('Choose one or more types for your prompt.'))

    # Output field (required, text field)
    # output = MarkdownxField(verbose_name=_('Example output'), help_text=_('Example output of your prompt.'))
    output = MDTextField(verbose_name=_('Example output'), help_text=_('Example output of your prompt.'))

    # Price dollar field (required, decimal field with two decimal places, minimum value of 0.01)
    price_dollar = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0.01)], verbose_name=_('Price (US Dollar)'), help_text=_('Set the price of your prompt in US dollars.'))

    # Price yuan field (required, decimal field with two decimal places, minimum value of 0.01)
    price_yuan = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0.01)], verbose_name=_('Price (Chinese Yuan)'), help_text=_('Set the price of your prompt in Chinese yuan.'))

    # Seller field (required, foreign key to User model, related name for reverse lookup)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='prompts', verbose_name=_('Seller'), help_text=_('The user who created and sells the prompt.'))

     # Created at field (required, date and time field, auto-populated with current date and time when a new instance is created)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'), help_text=_('The date and time when the prompt was uploaded.'))

    # Updated at field (required, date and time field, auto-populated with current date and time when an existing instance is updated)
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Ppdated at'), help_text=_('The date and time when the prompt was last updated.'))

    # Feedback field (optional, text field, can be blank or null)
    # feedback = models.TextField(blank=True, null=True, verbose_name=_('Feedback'), help_text=_('Feedbacks to the seller of the prompt.'))
    feedback = MDTextField(blank=True, null=True, verbose_name=_('Feedback'), help_text=_('Feedbacks to the seller of the prompt.'))

    # Approved field (required, boolean field, default to False, indicates whether the prompt is approved by an admin)
    approved = models.BooleanField(default=False, verbose_name=_('Approved'), help_text=_('Whether the prompt is approved by an admin or not.'))

    # Meta class for model options
    class Meta:
        # Verbose name and plural name for the model
        verbose_name = _('Prompt')
        verbose_name_plural = _('Prompts')

        # Ordering option for the model (by title)
        ordering = ('title',)

        # Include all fields in forms and serializers by default
        # fields = '__all__'

    # String representation of the model
    def __str__(self):
        # Return the title of the prompt
        return self.title

    # Define a get_absolute_url() method
    def get_absolute_url(self):
        # Return the URL for the prompt detail view with the prompt id as an argument
        return reverse('prompt-detail', args=[str(self.id)])

# # A class for storing the concrete instances of prompt templates or prompt sequences
# class Instance(models.Model):
#     # The content of the instance, which is a specific prompt or a prompt sequence
#     content = models.TextField()

#     # The prompt that this instance belongs to, which must be a prompt template or a prompt sequence
#     prompt = models.ForeignKey(Prompt, on_delete=models.CASCADE, related_name='instances')

#     # The date and time when the instance was created
#     created_at = models.DateTimeField(auto_now_add=True)

#     # The date and time when the instance was last updated
#     updated_at = models.DateTimeField(auto_now=True)

#     # Meta class for model options
#     class Meta:
#         # Verbose name and plural name for the model
#         verbose_name = _('Instance')
#         verbose_name_plural = _('Instances')

#     def __str__(self):
#         return self.content

# # Define a model for prompt templates
# class Template(models.Model):
#     # Title field (required, up to 100 characters)
#     title = models.CharField(_('title'), max_length=100)

#     # Content field (required, up to 500 characters, contains variables in curly braces)
#     content = models.CharField(_('content'), max_length=500)

#     # Category field (required, foreign key to Category model, related name for reverse lookup)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='templates')

#     # Language field (required, choices from English and Chinese)
#     LANGUAGE_CHOICES = (
#         ('en', 'English'),
#         ('zh', 'Chinese'),
#     )
#     language = models.CharField(_('language'), max_length=2, choices=LANGUAGE_CHOICES)

#     # Price field (required, decimal number with two decimal places, minimum value of 0.01)
#     price = models.DecimalField(_('price'), max_digits=6, decimal_places=2, validators=[MinValueValidator(0.01)])

#     # Seller field (required, foreign key to User model, related name for reverse lookup)
#     seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='templates')

#     # Approved field (boolean, default to False, indicates whether the template is approved by an admin)
#     approved = models.BooleanField(_('approved'), default=False)

#     # Meta class for model options
#     class Meta:
#         # Verbose name and plural name for the model
#         verbose_name = _('template')
#         verbose_name_plural = _('templates')

#         # Ordering option for the model (by title)
#         ordering = ('title',)

#     # String representation of the model
#     def __str__(self):
#         # Return the title of the template
#         return self.title

# # Define a model for specific prompts
# class Prompt(models.Model):
#     # Title field (required, up to 100 characters)
#     title = models.CharField(_('title'), max_length=100)

#     # Content field (required, up to 500 characters, does not contain variables)
#     content = models.CharField(_('content'), max_length=500)

#     # Template field (required, foreign key to Template model, related name for reverse lookup)
#     template = models.ForeignKey(Template, on_delete=models.CASCADE, related_name='prompts')

#     # Language field (required, choices from English and Chinese)
#     LANGUAGE_CHOICES = (
#         ('en', 'English'),
#         ('zh', 'Chinese'),
#     )
#     language = models.CharField(_('language'), max_length=2, choices=LANGUAGE_CHOICES)

#     # Price field (required, decimal number with two decimal places, minimum value of 0.01)
#     price = models.DecimalField(_('price'), max_digits=6, decimal_places=2, validators=[MinValueValidator(0.01)])

#     # Seller field (required, foreign key to User model, related name for reverse lookup)
#     seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='prompts')

#     # Approved field (boolean, default to False, indicates whether the prompt is approved by an admin)
#     approved = models.BooleanField(_('approved'), default=False)

#     # Meta class for model options
#     class Meta:
#         # Verbose name and plural name for the model
#         verbose_name = _('prompt')
#         verbose_name_plural = _('prompts')

#         # Ordering option for the model (by title)
#         ordering = ('title',)

#     # String representation of the model
#     def __str__(self):
#         # Return the title of the prompt
#         return self.title

# Define a model for prompt purchases
class Purchase(models.Model):
    # Buyer field (required, foreign key to User model, related name for reverse lookup)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='purchases')

    # Prompt field (required, foreign key to Prompt model, related name for reverse lookup)
    prompt = models.ForeignKey(Prompt, on_delete=models.CASCADE, related_name='purchases')

    # Date field (required, date and time of the purchase)
    date = models.DateTimeField(_('date'), auto_now_add=True)

    # Payment method field (required, choices from PayPal, Stripe, UnionPay or WeChatPay)
    PAYMENT_METHOD_CHOICES = (
        ('paypal', 'PayPal'),
        ('stripe', 'Stripe'),
        ('unionpay', 'UnionPay'),
        ('wechatpay', 'WeChatPay'),
    )
    payment_method = models.CharField(_('payment method'), max_length=10,
                                      choices=PAYMENT_METHOD_CHOICES)

    # Meta class for model options
    class Meta:
        # Verbose name and plural name for the model
        verbose_name = _('purchase')
        verbose_name_plural = _('purchases')

        # Ordering option for the model (by date in descending order)
        ordering = ('-date',)

    # String representation of the model
    def __str__(self):
        # Return the buyer and prompt of the purchase
        return f'{self.buyer} bought {self.prompt}'
