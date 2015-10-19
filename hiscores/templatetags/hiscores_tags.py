from django import template

register = template.Library()


@register.filter
def get_rank(page, loop_counter):
    """
    Calculates the player rank from current page and loop index.
    :param page: Current page number
    :param loop_counter: Loop index
    :return: rank
    """
    rank = page.start_index() + loop_counter
    return "{:,}".format(rank)


@register.filter
def display_skill(d, skill):
    """
    Display skill in template
    :param d: Dictionary
    :param skill: key
    :return: Grabs the key from the dictionary and formats it.
    """
    return "{:,}".format(d[skill])


@register.filter
def display_exp(d, skill):
    """
    Display exp of the specified skill in template
    :param d: Dictionary
    :param skill: skill
    :return: formatted exp value
    """
    skill_exp = skill + "_exp"
    return "{:,}".format(int(d[skill_exp]))


@register.filter
def get_exp(l, index):
    """
    Gets the 'exp' key from a list of dictionary
    :param l: The list
    :param index: List index
    :return: 'exp' key
    """
    return l[index]['exp']