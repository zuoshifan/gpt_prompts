from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django_filters.views import FilterView
# import mistune
from .models import Category, Prompt
from .forms import PromptForm

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

# Create a view for creating a prompt
@login_required(login_url="/accounts/login/")
def prompt_create(request):
    # If the request method is POST, process the form data
    if request.method == 'POST':
        # Create a form instance and populate it with the data from the request
        form = PromptForm(request.POST, request.FILES)
        # Check if the form is valid
        if form.is_valid():
            # Save the form data as a new prompt instance, but don't commit to the database yet
            prompt = form.save(commit=False)
            # Set the seller of the prompt to the current user
            prompt.seller = request.user
            # Save the prompt instance to the database
            prompt.save()
            form.save_m2m() # save the many-to-many data for the form
            # Add a success message to the request
            messages.success(request, 'Your prompt has been created successfully.')
            # Redirect to the prompt detail view
            return redirect(prompt.get_absolute_url())
    # If the request method is GET, create a blank form instance
    else:
        form = PromptForm()
    # Render the prompt create template with the form as context
    return render(request, 'prompts/prompt_create.html', {'form': form})

# Define a view for displaying the list of prompts
class PromptListView(FilterView):
    # Specify the model and template for the view
    model = Prompt
    template_name = 'prompts/prompt_list.html'

    # Specify the filterset class for the view
    # filterset_class = PromptFilter

    # Specify a list or a tuple of the fields that you want to include for the automatic construction of the filterset class
    filterset_fields = ['title', 'category', 'description', 'style', 'content', 'types', 'price_dollar', 'price_yuan', 'seller']

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

    # def get_context_data(self, **kwargs):
    #     context = super(PromptDetailView, self).get_context_data(**kwargs)
    #     context['output_html'] = mistune.markdown(context['object'].output, escape=False) if context['object'] else ''
    #     return context

def search(request):
  query = request.GET.get('q', '')
  prompts = Prompt.objects.filter(Q(title__icontains=query) | Q(description__icontains=query) | Q(content__icontains=query))
  context = {
    'query': query,
    'prompts': prompts
  }
  return render(request, 'prompts/search_results.html', context)
