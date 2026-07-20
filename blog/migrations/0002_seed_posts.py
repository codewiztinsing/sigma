from datetime import datetime, timezone as dt_timezone

from django.db import migrations

POSTS = [
    {
        'title': 'New Training Batch Launched for Youth in Renewable Energy',
        'slug': 'new-training-batch-launched-for-youth-in-renewable-energy',
        'excerpt': 'Sigma has launched its 46th training batch, equipping 25 young Ethiopians with practical skills in solar installation, biogas systems, and green manufacturing.',
        'published_at': datetime(2026, 7, 1, tzinfo=dt_timezone.utc),
    },
    {
        'title': 'Three New Enterprises Launched in Oromia Region',
        'slug': 'three-new-enterprises-launched-in-oromia-region',
        'excerpt': 'Our latest venture-building initiative has resulted in three sustainable enterprises focused on agro-processing and waste management, creating 45 new jobs.',
        'published_at': datetime(2026, 6, 1, tzinfo=dt_timezone.utc),
    },
    {
        'title': 'Sigma Partners with Addis Ababa University on Innovation Research',
        'slug': 'sigma-partners-with-addis-ababa-university-on-innovation-research',
        'excerpt': 'A new research collaboration will focus on developing affordable technologies for smallholder farmers and rural communities.',
        'published_at': datetime(2026, 5, 1, tzinfo=dt_timezone.utc),
    },
    {
        'title': 'Sigma Recognized for Innovation in Social Enterprise',
        'slug': 'sigma-recognized-for-innovation-in-social-enterprise',
        'excerpt': 'Our Innovation-to-Livelihood Venture Studio model has been recognized as a pioneering approach to sustainable development in Ethiopia.',
        'published_at': datetime(2026, 4, 1, tzinfo=dt_timezone.utc),
    },
    {
        'title': 'Community Biogas Project Reaches 500 Households',
        'slug': 'community-biogas-project-reaches-500-households',
        'excerpt': 'Our flagship biogas initiative has now provided clean cooking solutions to over 500 households, reducing deforestation and improving health outcomes.',
        'published_at': datetime(2026, 3, 1, tzinfo=dt_timezone.utc),
    },
    {
        'title': 'Women-Led Enterprises Thriving in Green Manufacturing',
        'slug': 'women-led-enterprises-thriving-in-green-manufacturing',
        'excerpt': 'Over 60% of enterprises supported by Sigma are now women-led, creating a new generation of female entrepreneurs in sustainable industries.',
        'published_at': datetime(2026, 2, 1, tzinfo=dt_timezone.utc),
    },
]


def seed_posts(apps, schema_editor):
    Post = apps.get_model('blog', 'Post')
    for post in POSTS:
        Post.objects.create(**post)


def remove_posts(apps, schema_editor):
    Post = apps.get_model('blog', 'Post')
    Post.objects.filter(slug__in=[p['slug'] for p in POSTS]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_posts, remove_posts),
    ]
