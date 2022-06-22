#!/usr/bin/env python3
import yara
import hashlib
import os
import subprocess

rule = yara.compile(filepath='./rule.yara')

print('source:')
src = input()
digest = hashlib.sha256(src.encode()).hexdigest()
binfile = f'/tmp/{digest}'
sourcefile = f'/tmp/{digest}.c'
devnull = open('/dev/null')

with open(sourcefile, mode='w') as f:
    f.write(src)

com = subprocess.run(['clang', '-static', '-o', binfile, sourcefile], cwd='/tmp', capture_output=True)

if com.returncode != 0:
    os.remove(sourcefile)
    print('Compile Error')
    exit(1)

try:
    matches = rule.match(binfile, timeout=1)
    
    if len(matches) > 0:
        os.remove(sourcefile)
        os.remove(binfile)
        print('Malicious binary detected!!!')
        print('Please not exploit me...')
    else:
        os.remove(sourcefile)
        print('Not matched. Have Fun!')
        subprocess.run([f'/tmp/{digest}'])
        os.remove(binfile)

except:
    os.remove(sourcefile)
    os.remove(binfile)
