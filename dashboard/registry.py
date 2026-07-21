from blog.models import Post
from contact.models import ContactMessage
from partners.models import PartnerCategory, PartnershipOpportunity
from projects.models import Project, ProjectCategory


class ModelConfig:
    """Describes how a model is listed/created/edited in the dashboard."""

    def __init__(self, model, label, list_fields, form_fields, can_create=True, can_edit=True,
                 detail_fields=None):
        self.model = model
        self.label = label
        self.list_fields = list_fields
        self.form_fields = form_fields
        self.can_create = can_create
        self.can_edit = can_edit
        self.detail_fields = detail_fields or list_fields

    @property
    def slug(self):
        return self.model._meta.model_name


REGISTRY = {
    config.slug: config
    for config in [
        ModelConfig(
            model=Post,
            label='Blog Posts',
            list_fields=['title', 'published_at', 'is_published'],
            form_fields=['title', 'slug', 'excerpt', 'body', 'image', 'published_at', 'is_published'],
        ),
        ModelConfig(
            model=PartnerCategory,
            label='Partner Categories',
            list_fields=['title', 'icon_class', 'order', 'is_active'],
            form_fields=['icon_class', 'title', 'description', 'order', 'is_active'],
        ),
        ModelConfig(
            model=PartnershipOpportunity,
            label='Partnership Opportunities',
            list_fields=['title', 'slug', 'icon_class', 'order', 'is_active'],
            form_fields=['slug', 'icon_class', 'title', 'description', 'order', 'is_active'],
        ),
        ModelConfig(
            model=ContactMessage,
            label='Contact Messages',
            list_fields=['name', 'email', 'subject', 'created_at'],
            form_fields=['name', 'email', 'phone', 'subject', 'message'],
            detail_fields=['name', 'email', 'phone', 'subject', 'message', 'created_at'],
            can_create=False,
            can_edit=False,
        ),
        ModelConfig(
            model=ProjectCategory,
            label='Project Categories',
            list_fields=['label', 'slug', 'order'],
            form_fields=['slug', 'label', 'order'],
        ),
        ModelConfig(
            model=Project,
            label='Projects',
            list_fields=['title', 'category', 'is_featured', 'order', 'is_active'],
            form_fields=[
                'title', 'description', 'category', 'location', 'image',
                'badge_text', 'badge_color', 'tags', 'is_featured', 'impact_summary',
                'stat_1_number', 'stat_1_label', 'stat_2_number', 'stat_2_label',
                'stat_3_number', 'stat_3_label', 'order', 'is_active',
            ],
        ),
    ]
}
