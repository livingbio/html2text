import os
import re

link_patterns = [
    re.compile(r'youtube\.com/embed/([\w\-\d]+)'),
    re.compile(r'youtube\.com/watch\?v=([\w\-\d]+)'),
]


def youtube_id(link):
    for p in link_patterns:
        m = p.findall(link)
        if m:
            return m[0]


def normalize_link(link):
    if os.path.exists(link):
        return link

    id = youtube_id(link)
    if id:
        return 'http://www.youtube.com/watch?v=%s' % id

    return link
