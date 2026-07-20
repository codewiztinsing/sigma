from django.db import migrations

CATEGORIES = [
    {
        'icon_class': 'fas fa-university',
        'title': 'Government & Public Sector',
        'description': 'Collaborate on policy development, innovation infrastructure, and programs that support national development goals.',
        'order': 1,
    },
    {
        'icon_class': 'fas fa-graduation-cap',
        'title': 'Universities & Research',
        'description': 'Connect academic research with practical application through joint projects, student programs, and technology transfer.',
        'order': 2,
    },
    {
        'icon_class': 'fas fa-hand-holding-dollar',
        'title': 'Development Partners',
        'description': 'Co-design and implement programs that create sustainable impact in livelihoods, jobs, and inclusive growth.',
        'order': 3,
    },
    {
        'icon_class': 'fas fa-industry',
        'title': 'Private Sector',
        'description': 'Access innovative technologies, skilled talent, and new market opportunities through enterprise partnerships.',
        'order': 4,
    },
    {
        'icon_class': 'fas fa-handshake',
        'title': 'Financial Institutions',
        'description': 'Support enterprise financing, investment readiness, and innovative financial products for underserved entrepreneurs.',
        'order': 5,
    },
    {
        'icon_class': 'fas fa-users',
        'title': 'Civil Society',
        'description': 'Work together to reach vulnerable communities and ensure inclusive participation in innovation and enterprise.',
        'order': 6,
    },
]


def seed_categories(apps, schema_editor):
    PartnerCategory = apps.get_model('partners', 'PartnerCategory')
    for category in CATEGORIES:
        PartnerCategory.objects.create(**category)


def remove_categories(apps, schema_editor):
    PartnerCategory = apps.get_model('partners', 'PartnerCategory')
    PartnerCategory.objects.filter(
        title__in=[c['title'] for c in CATEGORIES]
    ).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_categories, remove_categories),
    ]
