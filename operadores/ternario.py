lockdown = False
grana = 130

status = 'Em casa' if lockdown or grana <=100 else 'Uhuuuuuuuuuu'

print(status)

print(f'O status é: {status}')