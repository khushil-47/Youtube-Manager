file = open('youtube.txt','w')

try:
    file.write('How to become a backend developer')
    
finally:
    file.clos()

with open('youtube.txt','w') as file:
    file.write('chai aur code by Hitesh Sir')

