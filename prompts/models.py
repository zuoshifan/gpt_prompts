from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
# Define a model for prompt categories
class Category(models.Model):
    # Name field (required, unique, up to 50 characters)
    name = models.CharField(_('name'), max_length=50, unique=True)

    # Slug field (required, unique, up to 50 characters, used for URLs)
    slug = models.SlugField(_('slug'), max_length=50, unique=True)

    # Meta class for model options
    class Meta:
        # Verbose name and plural name for the model
        verbose_name = _('category')
        verbose_name_plural = _('categories')

        # Ordering option for the model (by name)
        ordering = ('name',)

    # String representation of the model
    def __str__(self):
        # Return the name of the category
        return self.name

# Define a model for prompt templates
class Template(models.Model):
    # Title field (required, up to 100 characters)
    title = models.CharField(_('title'), max_length=100)

    # Content field (required, up to 500 characters, contains variables in curly braces)
    content = models.CharField(_('content'), max_length=500)

    # Category field (required, foreign key to Category model, related name for reverse lookup)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='templates')

    # Language field (required, choices from English and Chinese)
    LANGUAGE_CHOICES = (
        ('en', 'English'),
        ('zh', 'Chinese'),
    )
    language = models.CharField(_('language'), max_length=2, choices=LANGUAGE_CHOICES)

    # Price field (required, decimal number with two decimal places, minimum value of 0.01)
    price = models.DecimalField(_('price'), max_digits=6, decimal_places=2, validators=[MinValueValidator(0.01)])

    # Seller field (required, foreign key to User model, related name for reverse lookup)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='templates')

    # Approved field (boolean, default to False, indicates whether the template is approved by an admin)
    approved = models.BooleanField(_('approved'), default=False)

    # Meta class for model options
    class Meta:
        # Verbose name and plural name for the model
        verbose_name = _('template')
        verbose_name_plural = _('templates')

        # Ordering option for the model (by title)
        ordering = ('title',)

    # String representation of the model
    def __str__(self):
        # Return the title of the template
        return self.title

# Define a model for specific prompts
class Prompt(models.Model):
    # Title field (required, up to 100 characters)
    title = models.CharField(_('title'), max_length=100)

    # Content field (required, up to 500 characters, does not contain variables)
    content = models.CharField(_('content'), max_length=500)

    # Template field (required, foreign key to Template model, related name for reverse lookup)
    template = models.ForeignKey(Template, on_delete=models.CASCADE, related_name='prompts')

    # Language field (required, choices from English and Chinese)
    LANGUAGE_CHOICES = (
        ('en', 'English'),
        ('zh', 'Chinese'),
    )
    language = models.CharField(_('language'), max_length=2, choices=LANGUAGE_CHOICES)

    # Price field (required, decimal number with two decimal places, minimum value of 0.01)
    price = models.DecimalField(_('price'), max_digits=6, decimal_places=2, validators=[MinValueValidator(0.01)])

    # Seller field (required, foreign key to User model, related name for reverse lookup)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='prompts')

    # Approved field (boolean, default to False, indicates whether the prompt is approved by an admin)
    approved = models.BooleanField(_('approved'), default=False)

    # Meta class for model options
    class Meta:
        # Verbose name and plural name for the model
        verbose_name = _('prompt')
        verbose_name_plural = _('prompts')

        # Ordering option for the model (by title)
        ordering = ('title',)

    # String representation of the model
    def __str__(self):
        # Return the title of the prompt
        return self.title

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
