import sys, os
INTERP = os.path.join(os.environ['HOME'], 'justinsuen.com', 'bin', 'python')
if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)
sys.path.append(os.getcwd())

from application import application
