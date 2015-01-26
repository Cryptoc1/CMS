#!/usr/bin/env python
from CMS import CMS

manager = CMS(hostname="localhost", username="test", password="test123", db="CMS")

print manager.get_all_posts()
