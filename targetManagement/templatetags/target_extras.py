from django import template

register = template.Library()


@register.filter
def in_category(products, category):
    # filtered = filter(lambda product: product.category == category, products)
    filtered = products.filter(category=category)
    print(len(list(filtered)))
    return len(list(filtered))
