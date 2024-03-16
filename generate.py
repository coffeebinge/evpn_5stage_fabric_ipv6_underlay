#!/user/bin/env python
import jinja2
import yaml
import os


if not os.path.exists('configs'):
    os.makedirs('configs')

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
## fyi: github copilot is amazing! It took the above 4 comments and ran with it... 
## I barely had to type more than a few letters

with open('access.list') as leafinv:
    leaves = leafinv.readlines()
with open('spine.list') as spineinv:
    spines = spineinv.readlines()
with open('core.list') as coreinv:
    cores = coreinv.readlines()
with open('border.list') as borderinv:
    borders = borderinv.readlines()

with open('global-parameters.yml') as global_yml:
    global_vars = yaml.safe_load(global_yml)
with open('credentials.yml') as cred_yml:
    cred_vars = yaml.safe_load(cred_yml)

for leaf in leaves:
    leaf = leaf.replace('\n', '')
    with open(leaf+'.yml') as leaf_yml:
        leaf_vars = yaml.safe_load(leaf_yml)
        f = open('configs/'+leaf+'.conf', 'w')
        print(access.render(GLOBAL=global_vars, CREDS=cred_vars, USERINPUT=leaf_vars), file=f)
        f.close()

for spine in spines:
    spine = spine.replace('\n', '')
    with open(spine+'.yml') as spine_yml:
        spine_vars = yaml.safe_load(spine_yml)
        f = open('configs/'+spine+'.conf', 'w')
        print(spine.render(GLOBAL=global_vars, CREDS=cred_vars, USERINPUT=spine_vars), file=f)
        f.close()

for core in cores:
    core = core.replace('\n', '')
    with open(core+'.yml') as core_yml:
        core_vars = yaml.safe_load(core_yml)
        f = open('configs/'+core+'.conf', 'w')
        print(core.render(GLOBAL=global_vars, CREDS=cred_vars, USERINPUT=core_vars), file=f)
        f.close()

for border in borders:
    border = border.replace('\n', '')
    with open(border+'.yml') as border_yml:
        border_vars = yaml.safe_load(border_yml)
        f = open('configs/'+border+'.conf', 'w')
        print(border.render(GLOBAL=global_vars, CREDS=cred_vars, USERINPUT=border_vars), file=f)
        f.close()   
