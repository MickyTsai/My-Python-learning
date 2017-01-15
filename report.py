def get_description(): # see the docstring below?
    """Reture random weather, just like the pros"""
    from random import choice
    possibilities = ['rain','now','fog','sun','who knows']
    return choice(possibilities)
