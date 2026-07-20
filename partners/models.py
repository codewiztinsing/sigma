from django.db import models


class PartnerCategory(models.Model):
    icon_class = models.CharField(
        max_length=50,
        help_text="Font Awesome class, e.g. 'fas fa-university'",
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order', 'id']
        verbose_name_plural = 'Partner categories'

    def __str__(self):
        return self.title


class PartnershipOpportunity(models.Model):
    slug = models.SlugField(
        max_length=50,
        unique=True,
        help_text="Used as the value in the partnership type dropdown, e.g. 'funding'",
    )
    icon_class = models.CharField(
        max_length=50,
        help_text="Font Awesome class, e.g. 'fas fa-hand-holding-dollar'",
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order', 'id']
        verbose_name_plural = 'Partnership opportunities'

    def __str__(self):
        return self.title
