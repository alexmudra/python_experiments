'''
This somewhat depends on what platform you are on. The most common way to do this is by printing ANSI escape sequences.
For a simple example, here's some python code from the blender build scripts:
'''



class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print (bcolors.WARNING + "Warning: No active frommets remain. Continue?" + bcolors.ENDC)