# Import modules and functions
from django.urls import path
# from django.conf.urls.i18n import i18n_patterns

from . import views

# Define URL patterns
urlpatterns = [
    # URL pattern for home view (path: '')
    path('', views.home, name='home'),

    # URL pattern for about view (path: 'about/')
    path('about/', views.about, name='about'),

    # URL pattern for search results
    path('search/', views.search, name='search'),

    # # URL pattern for template list view (path: 'templates/')
    # path('templates/', views.TemplateListView.as_view(), name='template-list'),

    # # URL pattern for template detail view (path: 'templates/<int:pk>/')
    # path('templates/<int:pk>/', views.TemplateDetailView.as_view(), name='template-detail'),

    # # URL pattern for template create view (path: 'templates/new/')
    # path('templates/new/', views.TemplateCreateView.as_view(), name='template-create'),

    # # URL pattern for template update view (path: 'templates/<int:pk>/update/')
    # path('templates/<int:pk>/update/', views.TemplateUpdateView.as_view(), name='template-update'),

    # # URL pattern for template delete view (path: 'templates/<int:pk>/delete/')
    # path('templates/<int:pk>/delete/', views.TemplateDeleteView.as_view(), name='template-delete'),

    # URL pattern for prompt list view (path: 'prompts/')
    path('prompts/', views.PromptListView.as_view(), name='prompt-list'),

    # URL pattern for prompt detail view (path: 'prompts/<int:pk>/')
    path('prompts/<int:pk>/', views.PromptDetailView.as_view(), name='prompt-detail'),

    # URL pattern for prompt create view (path: 'prompts/new/')
    # path('prompts/new/', views.PromptCreateView.as_view(), name='prompt-create'),
    # path('prompts/new/', views.create_prompt, name='prompt-create'),
    path('prompts/create/', views.prompt_create, name='prompt-create'),

    # URL pattern for prompt update view (path: 'prompts/<int:pk>/update/')
    # path('prompts/<int:pk>/update/', views.PromptUpdateView.as_view(), name='prompt-update'),

    # URL pattern for prompt delete view (path: 'prompts/<int:pk>/delete/')
    # path('prompts/<int:pk>/delete/', views.PromptDeleteView.as_view(), name='prompt-delete'),

    # URL pattern for prompt upload view (path: 'prompts/upload/')
    # path('prompts/upload/', views.upload_prompt, name='prompt-upload'),

    # # URL pattern for prompt buy view (path: 'prompts/<int:pk>/buy/')
    # path('prompts/<int:pk>/buy/', views.buy_prompt, name='prompt-buy'),

    # URL pattern for prompt feedback create view (path: 'prompts/<int:pk>/feedback/')
    # path('prompts/<int:pk>/feedback/', views.PromptFeedbackCreateView.as_view(), name='prompt-feedback-create'),

    # URL pattern for prompt feedback update view (path: 'prompts/<int:pk>/feedback/update/')
    # path('prompts/<int:pk>/feedback/update/', views.PromptFeedbackUpdateView.as_view(), name='prompt-feedback-update'),
]
