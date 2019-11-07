import os
from glob import glob
import sys

path = sys.argv[1]
decompiler = sys.argv[2]

result = [y for x in os.walk(path) for y in glob(os.path.join(x[0], '*.luac'))]
for f in result:
    print(f)
    os.system("java -jar %s %s > %s.lua" % (decompiler, f, os.path.splitext(f)[0]))
    os.system("del /f %s" % f)