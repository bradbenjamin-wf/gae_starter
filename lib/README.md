The lib folder is a little confusing.  It is for dependencies, but it has to fill 2 purposes:
1. Local development dependencies
2. Supply Dependencies so they are uploaded on deploy, you do not run 'pip install' on the app engine machines

When you pip install with a "-t lib/" at the end, it's not going to install to your python site-packages folder, but rather just dump the dependencies to lib/.

The idea is that you wouldn't have to check in those pip-generated folders in lib, but you do need them before you deploy new code.
