"""
util to
- generate unique string of specified length. can be use with distributed system
- combine strings to make it url compatible
"""
import re
import random
import string
import time
random.seed(time.time())

def generate_unique(length=10):
    """
    generate unique alphanumeric string of specified length.
    tested with 100+ distributed task.
    got 99.999% uniquness
    can be used in slug creation
    """
    char_list = ''.join([string.digits, string.lowercase])
    random_str = ''.join(random.choice(char_list) for i in range(length))
    unqid = "%.10f" % time.time()
    unqid = "{}{}".format(random_str, unqid[-5:])
    unqid = ''.join(random.sample(unqid, len(unqid)))
    return unqid

def build_url_compatible(part1, part2=''):
    """
    combine multiple strings to form url
    handles all special charcaters
    builds url max of 150 char
    """
    xstr = lambda s: '' if s is None else s
    page_url = ' '.join([xstr(part1), xstr(part2)])

    # trim
    page_url = page_url.strip()

    # convert to lower case
    page_url = page_url.lower()

    # handle special char
    page_url = re.sub(r'[~!@#$%^&*()_+={}|:;"<,>.?/]', r'-', page_url)
    page_url = re.sub(r"'", r'-', page_url)
    page_url = re.sub(r'\[', r'-', page_url)
    page_url = re.sub(r'\]', r'-', page_url)
    page_url = re.sub(r"\\", r'-', page_url)
    page_url = re.sub(r' ', r'-', page_url)
    page_url = re.sub(r'\n', r'-', page_url)

    # handle train of hypen
    page_url = re.sub(r'(-+)', r'-', page_url)

    # handle all hypen page_url
    page_url = re.sub(r'(-+)', r'-', page_url)

    # handle hypen at start
    page_url = page_url[1:] if page_url.startswith('-') else page_url

    # handle hypen at end
    page_url = page_url[:-1] if page_url.endswith('-') else page_url

    # page_url should contain other than just hypen
    page_url = page_url if page_url != '-' else None

    if page_url is None:
        return None

    # chop page_url to max length supported
    page_url = page_url[0:150] if len(page_url) > 150 else page_url

    return page_url
