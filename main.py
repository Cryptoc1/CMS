#!/usr/bin/env python
from CMS import CMS
from CMS import Post

manager = CMS(hostname="localhost", username="test", password="test123", db="CMS")

print type(manager.get_all_posts())
