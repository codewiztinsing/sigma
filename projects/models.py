from django.db import models

BADGE_COLOR_CHOICES = [
    ('green', 'Green'),
    ('blue', 'Blue'),
    ('dark-green', 'Dark Green'),
]


class ProjectCategory(models.Model):
    slug = models.SlugField(
        max_length=50,
        unique=True,
        help_text="Used as the filter value, e.g. 'green'",
    )
    label = models.CharField(max_length=100, help_text="Shown on the filter button, e.g. 'Green Tech'")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'id']
        verbose_name_plural = 'Project categories'

    def __str__(self):
        return self.label


class Project(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    category = models.ForeignKey(ProjectCategory, on_delete=models.PROTECT, related_name='projects')
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    badge_text = models.CharField(max_length=50, help_text="Small badge label, e.g. 'Circular Economy'")
    badge_color = models.CharField(max_length=20, choices=BADGE_COLOR_CHOICES, default='green')
    tags = models.CharField(max_length=200, help_text="Comma-separated, e.g. 'Recycling, Green Manufacturing'")

    is_featured = models.BooleanField(default=False, help_text="Show in the Featured Project highlight instead of the grid.")
    impact_summary = models.CharField(
        max_length=200, blank=True,
        help_text="Only used when featured, e.g. '35 enterprises created, 1,200+ jobs generated, 15+ communities reached.'",
    )
    stat_1_number = models.CharField(max_length=20, blank=True, help_text="e.g. '35' (featured only)")
    stat_1_label = models.CharField(max_length=50, blank=True, help_text="e.g. 'Enterprises' (featured only)")
    stat_2_number = models.CharField(max_length=20, blank=True)
    stat_2_label = models.CharField(max_length=50, blank=True)
    stat_3_number = models.CharField(max_length=20, blank=True)
    stat_3_label = models.CharField(max_length=50, blank=True)

    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return self.title

    def tag_list(self):
        return [tag.strip() for tag in self.tags.split(',') if tag.strip()]
