from django.db import migrations

OPPORTUNITIES = [
    {
        'slug': 'funding',
        'icon_class': 'fas fa-hand-holding-dollar',
        'title': 'Program Funding',
        'description': 'Support specific programs in training, enterprise development, technology innovation, or ecosystem building.',
        'order': 1,
    },
    {
        'slug': 'research',
        'icon_class': 'fas fa-flask',
        'title': 'Research Collaboration',
        'description': 'Joint research projects that combine academic rigor with practical application for community impact.',
        'order': 2,
    },
    {
        'slug': 'infrastructure',
        'icon_class': 'fas fa-building',
        'title': 'Infrastructure Support',
        'description': 'Provide or fund innovation spaces, fabrication facilities, laboratories, and testing equipment.',
        'order': 3,
    },
    {
        'slug': 'investment',
        'icon_class': 'fas fa-chart-line',
        'title': 'Investment & Finance',
        'description': 'Invest in or provide financing for enterprises that have demonstrated technical and commercial viability.',
        'order': 4,
    },
    {
        'slug': 'technical',
        'icon_class': 'fas fa-people-arrows',
        'title': 'Technical Expertise',
        'description': 'Contribute engineering, design, business, or sector-specific expertise as mentors or advisors.',
        'order': 5,
    },
    {
        'slug': 'market',
        'icon_class': 'fas fa-globe',
        'title': 'Market Access',
        'description': 'Provide distribution channels, procurement opportunities, or market linkages for enterprises we build.',
        'order': 6,
    },
]


def seed_opportunities(apps, schema_editor):
    PartnershipOpportunity = apps.get_model('partners', 'PartnershipOpportunity')
    for opportunity in OPPORTUNITIES:
        PartnershipOpportunity.objects.create(**opportunity)


def remove_opportunities(apps, schema_editor):
    PartnershipOpportunity = apps.get_model('partners', 'PartnershipOpportunity')
    PartnershipOpportunity.objects.filter(
        slug__in=[o['slug'] for o in OPPORTUNITIES]
    ).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0003_partnershipopportunity'),
    ]

    operations = [
        migrations.RunPython(seed_opportunities, remove_opportunities),
    ]
