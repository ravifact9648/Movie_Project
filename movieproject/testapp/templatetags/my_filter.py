from django import template
register=template.Library()
def capitalize(value):
    return value[0].upper()+value[1::]
register.filter('cap',capitalize)
