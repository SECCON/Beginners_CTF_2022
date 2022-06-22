import subprocess

chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

for a in chars:
    for b in chars:
        for c in chars:
            print(f'http://localhost:8080/{a}{b}{c}')
