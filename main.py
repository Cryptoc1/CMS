#!/usr/bin/env python
from CMS import CMS

manager = CMS(hostname="localhost", username="test", password="test123", db="")
manager.set_db("CMStest")

# print manager."method"
