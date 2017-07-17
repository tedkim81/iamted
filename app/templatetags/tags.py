from django import template

register = template.Library()

@register.simple_tag
def get_title(obj, arg):
    return obj.get_title(arg)

@register.simple_tag
def get_key_str(obj, arg):
    return obj.get_key_str(arg)

@register.simple_tag
def get_value_str(obj, arg):
    return obj.get_value_str(arg)

@register.simple_tag
def get_company(obj, arg):
    return obj.get_company(arg)

@register.simple_tag
def get_name(obj, arg):
    return obj.get_name(arg)

@register.simple_tag
def get_position(obj, arg):
    return obj.get_position(arg)

@register.simple_tag
def get_intro(obj, arg):
    return obj.get_intro(arg)
