from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.forms import modelform_factory
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render

from .registry import REGISTRY


def is_staff_user(user):
    return user.is_active and user.is_staff


def dashboard_login(request):
    if request.user.is_authenticated and is_staff_user(request.user):
        return redirect('dashboard_home')

    error = None
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user is not None and is_staff_user(user):
            login(request, user)
            return redirect('dashboard_home')
        error = 'Invalid credentials or insufficient permissions.'

    return render(request, 'dashboard/login.html', {'error': error})


def dashboard_logout(request):
    logout(request)
    return redirect('dashboard_login')


@login_required(login_url='dashboard_login')
@user_passes_test(is_staff_user, login_url='dashboard_login')
def dashboard_home(request):
    cards = [
        {'slug': slug, 'config': config, 'count': config.model.objects.count()}
        for slug, config in REGISTRY.items()
    ]
    return render(request, 'dashboard/home.html', {
        'registry': REGISTRY,
        'cards': cards,
    })


def _get_config_or_404(model_slug):
    config = REGISTRY.get(model_slug)
    if config is None:
        raise Http404('Unknown model')
    return config


@login_required(login_url='dashboard_login')
@user_passes_test(is_staff_user, login_url='dashboard_login')
def model_list(request, model_slug):
    config = _get_config_or_404(model_slug)
    objects = config.model.objects.all()
    return render(request, 'dashboard/model_list.html', {
        'registry': REGISTRY,
        'model_slug': model_slug,
        'config': config,
        'objects': objects,
    })


@login_required(login_url='dashboard_login')
@user_passes_test(is_staff_user, login_url='dashboard_login')
def model_create(request, model_slug):
    config = _get_config_or_404(model_slug)
    if not config.can_create:
        raise Http404('This model does not support creation.')

    form_class = modelform_factory(config.model, fields=config.form_fields)
    if request.method == 'POST':
        form = form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Created successfully.')
            return redirect('dashboard_model_list', model_slug=model_slug)
    else:
        form = form_class()

    return render(request, 'dashboard/model_form.html', {
        'registry': REGISTRY,
        'model_slug': model_slug,
        'config': config,
        'form': form,
        'is_create': True,
    })


@login_required(login_url='dashboard_login')
@user_passes_test(is_staff_user, login_url='dashboard_login')
def model_edit(request, model_slug, pk):
    config = _get_config_or_404(model_slug)
    if not config.can_edit:
        raise Http404('This model does not support editing.')

    instance = get_object_or_404(config.model, pk=pk)
    form_class = modelform_factory(config.model, fields=config.form_fields)
    if request.method == 'POST':
        form = form_class(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            messages.success(request, 'Changes saved.')
            return redirect('dashboard_model_list', model_slug=model_slug)
    else:
        form = form_class(instance=instance)

    return render(request, 'dashboard/model_form.html', {
        'registry': REGISTRY,
        'model_slug': model_slug,
        'config': config,
        'form': form,
        'is_create': False,
        'instance': instance,
    })


@login_required(login_url='dashboard_login')
@user_passes_test(is_staff_user, login_url='dashboard_login')
def model_delete(request, model_slug, pk):
    config = _get_config_or_404(model_slug)
    instance = get_object_or_404(config.model, pk=pk)

    if request.method == 'POST':
        instance.delete()
        messages.success(request, 'Deleted.')
        return redirect('dashboard_model_list', model_slug=model_slug)

    return render(request, 'dashboard/model_confirm_delete.html', {
        'registry': REGISTRY,
        'model_slug': model_slug,
        'config': config,
        'instance': instance,
    })
