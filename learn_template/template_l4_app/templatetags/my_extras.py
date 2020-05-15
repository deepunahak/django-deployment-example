from django import template

register = template.Library()


# use decorator
@register.filter(name='change_str')
def change_str(value, arg):
    """
    This cuts out all value of 'arg' from the string
    :param value:
    :param arg:
    :return: call built-in replace() function
    """
    return value.replace(arg, '')


# OR #
# manually do this line
# register.filter('cut', cut)
