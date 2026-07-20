from django import template

register = template.Library()


@register.filter
def get_attr(obj, field_name):
    value = getattr(obj, field_name, '')
    if callable(value):
        value = value()
    return value


@register.filter
def field_label(model, field_name):
    try:
        return model._meta.get_field(field_name).verbose_name.title()
    except Exception:
        return field_name.replace('_', ' ').title()
