import re

home_html = []
with open('home.html', 'rb') as f:
    home_html = f.readlines()

updated_html = []
for line in home_html:
    if 'option name' in line:
        line = re.sub(re.findall('value="(.*?)"', line)[0],
                      re.findall('name="(.*?)"', line)[0], line)
    updated_html.append(line)

with open('new_home.html', 'wb') as f:
    for l in updated_html:
        f.write(l)
        
