from django.db import migrations

CATEGORIES = [
    {'slug': 'green', 'label': 'Green Tech', 'order': 1},
    {'slug': 'agriculture', 'label': 'Agriculture', 'order': 2},
    {'slug': 'energy', 'label': 'Energy', 'order': 3},
    {'slug': 'manufacturing', 'label': 'Manufacturing', 'order': 4},
]

PROJECTS = [
    {
        'title': 'Innovation-to-Livelihood Venture Studio',
        'description': (
            'Our flagship program transforms community livelihood challenges into sustainable '
            'enterprises through a systematic eight-stage process. From identifying unmet needs '
            'to scaling proven models, we build businesses that create jobs and improve lives.'
        ),
        'category_slug': 'green',
        'location': 'Transforming challenges into enterprises',
        'badge_text': 'Flagship Initiative',
        'badge_color': 'green',
        'tags': '',
        'is_featured': True,
        'impact_summary': '35 enterprises created, 1,200+ jobs generated, 15+ communities reached.',
        'stat_1_number': '35', 'stat_1_label': 'Enterprises',
        'stat_2_number': '1,200+', 'stat_2_label': 'Jobs',
        'stat_3_number': '15+', 'stat_3_label': 'Communities',
        'order': 0,
    },
    {
        'title': 'Waste-to-Value Initiative',
        'description': 'Transforming agricultural and plastic waste into valuable products through innovative recycling and upcycling technologies.',
        'category_slug': 'green',
        'location': 'Addis Ababa',
        'badge_text': 'Circular Economy',
        'badge_color': 'green',
        'tags': 'Recycling, Green Manufacturing',
        'order': 1,
    },
    {
        'title': 'Solar-Powered Irrigation Systems',
        'description': 'Affordable solar irrigation solutions that increase crop yields, reduce water waste, and improve farmer incomes.',
        'category_slug': 'agriculture',
        'location': 'Oromia Region',
        'badge_text': 'Agro-processing',
        'badge_color': 'blue',
        'tags': 'Renewable Energy, Agriculture',
        'order': 2,
    },
    {
        'title': 'Community Biogas Digesters',
        'description': 'Household and community-scale biogas systems that convert organic waste into clean cooking fuel and organic fertilizer.',
        'category_slug': 'energy',
        'location': 'Amhara Region',
        'badge_text': 'Clean Energy',
        'badge_color': 'dark-green',
        'tags': 'Biogas, Rural Development',
        'order': 3,
    },
    {
        'title': 'Eco-Friendly Building Materials',
        'description': 'Developing locally manufactured sustainable construction materials from recycled and natural resources.',
        'category_slug': 'manufacturing',
        'location': 'Addis Ababa',
        'badge_text': 'Construction',
        'badge_color': 'blue',
        'tags': 'Green Construction, Manufacturing',
        'order': 4,
    },
    {
        'title': 'Post-Harvest Processing Equipment',
        'description': 'Affordable processing machinery that reduces food losses, improves quality, and increases farmer incomes.',
        'category_slug': 'agriculture',
        'location': 'SNNPR',
        'badge_text': 'Agro-processing',
        'badge_color': 'green',
        'tags': 'Food Security, Manufacturing',
        'order': 5,
    },
    {
        'title': 'Rural Digital Innovation Hub',
        'description': 'Technology centers providing digital skills training, internet access, and innovation support for rural youth and entrepreneurs.',
        'category_slug': 'green',
        'location': 'Multiple Regions',
        'badge_text': 'Digital Innovation',
        'badge_color': 'blue',
        'tags': 'Digital, Youth Empowerment',
        'order': 6,
    },
]


def seed_projects(apps, schema_editor):
    ProjectCategory = apps.get_model('projects', 'ProjectCategory')
    Project = apps.get_model('projects', 'Project')

    categories_by_slug = {}
    for cat in CATEGORIES:
        obj = ProjectCategory.objects.create(**cat)
        categories_by_slug[cat['slug']] = obj

    for project in PROJECTS:
        data = dict(project)
        category_slug = data.pop('category_slug')
        data['category'] = categories_by_slug[category_slug]
        Project.objects.create(**data)


def remove_projects(apps, schema_editor):
    Project = apps.get_model('projects', 'Project')
    ProjectCategory = apps.get_model('projects', 'ProjectCategory')
    Project.objects.filter(title__in=[p['title'] for p in PROJECTS]).delete()
    ProjectCategory.objects.filter(slug__in=[c['slug'] for c in CATEGORIES]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_projects, remove_projects),
    ]
