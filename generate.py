#!/user/bin/env python
import jinja2
import yaml
import sys


loader = jinja2.FileSystemLoader(searchpath="./jinja")
jenv = jinja2.Environment(loader=loader, trim_blocks=True, lstrip_blocks=True)

access = jenv.get_template("jinja/access_leaf.j2")
spine = jenv.get_template("jinja/spine.j2")
core = jenv.get_template("jinja/core.j2")
border = jenv.get_template("jinja/border.j2")


## get a list of devies by template type
## define input params separating variables by group.. GLOBAL, CREDS, USERINPUT. 
## render template config output into ./config directory
## render leaves, core/spine and border leaves separately