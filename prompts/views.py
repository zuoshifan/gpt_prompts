from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.translation import gettext_lazy as _
from django_filters.views import FilterView
# from feedback.models import FeedbackBaseModelMixin, FeedbackModelMixin, FeedbackFormMixin, FeedbackMessageMixin, FeedbackSuccessURLMixin, FeedbackViewMixin, FeedbackDeleteViewMixin, FeedbackUpdateViewMixin, FeedbackCreateViewMixin, FeedbackListViewMixin, FeedbackDetailViewMixin

from .models import Category, Template, Prompt, Purchase
from .forms import TemplateCreateForm, PromptCreateForm

# Create your views here.
# Define a function to check if a user is an admin or not
def is_admin(user):
    # Return True if user is an admin or False otherwise
    return user.is_superuser

# Define a view for displaying the home page of the website
def home(request):
    # Render the home.html template with some context data
    return render(request, 'prompts/home.html', {
        # Pass the categories as context data
        'categories': Category.objects.all(),
    })

# Define a view for displaying the about page of the website
def about(request):
    # Render the about.html template with no context data
    return render(request, 'prompts/about.html')

# Define a view for displaying the list of templates
class TemplateListView(FilterView):
    # Specify the model and template for the view
    model = Template
    template_name = 'prompts/template_list.html'

    # Specify the filterset class for the view
    # filterset_class = TemplateFilter

    # Specify the context object name for the view
    context_object_name = 'templates'

    # Specify the ordering option for the view (by title)
    ordering = 'title'

    # Specify the paginate by option for the view (10 items per page)
    paginate_by = 10

# Define a view for displaying the detail of a template
class TemplateDetailView(DetailView):
    # Specify the model and template for the view
    model = Template
    template_name = 'prompts/template_detail.html'

# Define a view for creating a template
class TemplateCreateView(LoginRequiredMixin, CreateView):
    # Specify the model and form class for the view
    model = Template
    form_class = TemplateCreateForm

    # Specify the template for the view
    template_name = 'prompts/template_form.html'

    # Override the form valid method to set the seller field to the current user
    def form_valid(self, form):
        # Set the seller field to the current user
        form.instance.seller = self.request.user

        # Call the super method to save the form and return a response
        return super().form_valid(form)

# Define a view for updating a template
class TemplateUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    # Specify the model and form class for the view
    model = Template
    form_class = TemplateCreateForm

    # Specify the template for the view
    template_name = 'prompts/template_form.html'

    # Override the form valid method to set the seller field to the current user
    def form_valid(self, form):
        # Set the seller field to the current user
        form.instance.seller = self.request.user

        # Call the super method to save the form and return a response
        return super().form_valid(form)

    # Override the test func method to check if the current user is the seller of the template or an admin
    def test_func(self):
        # Get the template object from the view
        template = self.get_object()

        # Return True if the current user is the seller of the template or an admin or False otherwise
        return self.request.user == template.seller or is_admin(self.request.user)

# Define a view for deleting a template
class TemplateDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    # Specify the model and template for the view
    model = Template
    template_name = 'prompts/template_confirm_delete.html'

    # Specify the success URL for the view (redirect to template list)
    success_url = '/templates/'

    # Override the test func method to check if the current user is the seller of the template or an admin
    def test_func(self):
        # Get the template object from the view
        template = self.get_object()

        # Return True if the current user is the seller of the template or an admin or False otherwise
        return self.request.user == template.seller or is_admin(self.request.user)

# Define a view for displaying the list of prompts
class PromptListView(FilterView):
    # Specify the model and template for the view
    model = Prompt
    template_name = 'prompts/prompt_list.html'

    # Specify the filterset class for the view
    # filterset_class = PromptFilter

    # Specify the context object name for the view
    context_object_name = 'prompts'

    # Specify the ordering option for the view (by title)
    ordering = 'title'

    # Specify the paginate by option for the view (10 items per page)
    paginate_by = 10

# Define a view for displaying the detail of a prompt
class PromptDetailView(DetailView):
    # Specify the model and template for the view
    model = Prompt
    template_name = 'prompts/prompt_detail.html'

# Define a view for creating a prompt
class PromptCreateView(LoginRequiredMixin, CreateView):
    # Specify the model and form class for the view
    model = Prompt
    form_class = PromptCreateForm

    # Specify the template for the view
    template_name = 'prompts/prompt_form.html'

    # Override the form valid method to set the seller field to the current user
    def form_valid(self, form):
        # Set the seller field to the current user
        form.instance.seller = self.request.user

        # Call the super method to save the form and return a response
        return super().form_valid(form)

# Define a view for updating a prompt
class PromptUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    # Specify the model and form class for the view
    model = Prompt
    form_class = PromptCreateForm

    # Specify the template for the view
    template_name = 'prompts/prompt_form.html'

    # Override the form valid method to set the seller field to the current user
    def form_valid(self, form):
        # Set the seller field to the current user
        form.instance.seller = self.request.user

        # Call the super method to save the form and return a response
        return super().form_valid(form)

    # Override the test func method to check if the current user is the seller of the prompt or an admin
    def test_func(self):
        # Get the prompt object from the view
        prompt = self.get_object()

        # Return True if the current user is the seller of the prompt or an admin or False otherwise
        return self.request.user == prompt.seller or is_admin(self.request.user)

# Define a view for deleting a prompt
class PromptDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    # Specify the model and template for the view
    model = Prompt
    template_name = 'prompts/prompt_confirm_delete.html'

    # Specify the success URL for the view (redirect to prompt list)
    success_url = '/prompts/'

    # Override the test func method to check if the current user is the seller of the prompt or an admin
    def test_func(self):
        # Get the prompt object from the view
        prompt = self.get_object()

        # Return True if the current user is the seller of the prompt or an admin or False otherwise
        return self.request.user == prompt.seller or is_admin(self.request.user)

# Define a view for buying a prompt
@login_required
def buy_prompt(request, pk):
    # Get the prompt object by primary key or raise 404 error if not found
    prompt = get_object_or_404(Prompt, pk=pk)

    # Check if the user has already bought the prompt or not
    if Purchase.objects.filter(buyer=request.user, prompt=prompt).exists():
        # If yes, display a message and redirect to prompt detail page
        messages.warning(request, _('You have already bought this prompt.'))
        return redirect('prompt-detail', pk=pk)
    else:
        # If no, create a new purchase object and save it to the database
        purchase = Purchase(buyer=request.user, prompt=prompt)
        purchase.save()

        # Display a message and redirect to prompt detail page
        messages.success(request, _('You have successfully bought this prompt.'))
        return redirect('prompt-detail', pk=pk)

# # Define a view for rating and reviewing a prompt
# class PromptFeedbackCreateView(LoginRequiredMixin, FeedbackBaseModelMixin, FeedbackModelMixin, FeedbackFormMixin,
#                                FeedbackMessageMixin, FeedbackSuccessURLMixin, FeedbackCreateViewMixin):
#     # Specify the model and form class for feedback
#     model = Prompt
#     form_class = PromptFeedbackForm

#     # Specify the template for feedback
#     template_name = 'prompts/prompt_feedback_form.html'

#     # Specify the success message for feedback
#     success_message = _('Thank you for your feedback.')

#     # Override the get success URL method to return to prompt detail page
#     def get_success_url(self):
#         # Return to prompt detail page with primary key
#         return reverse('prompt-detail', kwargs={'pk': self.object.pk})

# # Define a view for updating rating and review of a prompt
# class PromptFeedbackUpdateView(LoginRequiredMixin, UserPassesTestMixin, FeedbackBaseModelMixin, FeedbackModelMixin,
#                                FeedbackFormMixin, FeedbackMessageMixin, FeedbackSuccessURLMixin,
#                                FeedbackUpdateViewMixin):
#     # Specify the model and form class for feedback
#     model = Prompt
#     form_class = PromptFeedbackForm

#     # Specify the template for feedback
#     template_name = 'prompts/prompt_feedback_form.html'

#     # Specify the success message for feedback
#     success_message = _('Your feedback has been updated.')

#     # Override the get success URL method to return to prompt detail page
#     def get_success_url(self):
#         # Return to prompt detail page with primary key
#         return reverse('prompt-detail', kwargs={'pk': self.object.pk})

#     # Override the test func method to check if the current user is the rater of the feedback or an admin
#     def test_func(self):
#         # Get the feedback object from the view
#         feedback = self.get_object()

#         # Return True if the current user is the rater of the feedback or an admin or False otherwise
#         return self.request.user == feedback.rater or is_admin(self.request.user)
