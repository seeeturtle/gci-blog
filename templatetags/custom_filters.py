from statik.templatetags import register

@register.filter(name='slugify')
def filter_slugify(s):
    return '-'.join(w.lower() for w in s.split(' '))
