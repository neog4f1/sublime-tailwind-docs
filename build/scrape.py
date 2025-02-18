# i add this
from urllib.request import urlopen, Request
import re
url = 'https://tailwindcss.com/docs/installation'
req = Request(
        url,
        data=None,
        headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) ' +
            'AppleWebKit/537.36 (KHTML, like Gecko) ' +
            'Chrome/35.0.1916.47 Safari/537.36'
        }
    )
# req.add_header('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0')
response = docs = urlopen(req).read().decode('utf-8')
links = re.findall('href="(?:(?<=href="))([^"]*\/docs\/[^"]*)(?=")"', response)
print(len(set(links)))

# i add this


import re
import json
import urllib.request


# Create a request with a valid User-Agent
req = urllib.request.Request(
    'https://tailwindcss.com/docs/',
    data=None,
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) ' +
        'AppleWebKit/537.36 (KHTML, like Gecko) ' +
        'Chrome/35.0.1916.47 Safari/537.36'
    }
)

# Pull the html from the main docs page and find all /docs links
docs = urllib.request.urlopen(req)
links = re.findall('href="(.+?tailwindcss\.com/docs/.*?)"', docs.read().decode('utf-8'))
found = []

# Format each link as a sublime command, regenerate the command file
with open('../Default.sublime-commands', 'w+') as f:
    f.write('[\n')
    first = True
    for url in set(links):
    # for url in sorted(set(links)):

        url = url.replace('https://tailwindcss.com', '')
        topic = url.split('/')[2].title().replace('-', ' ').split('#')[0]
        slug = url.split('/')[2].split('#')[0]

        if (topic not in found):
            found.append(topic)

            if not first:
                f.write(', \n    ')
            else:
                f.write('    ')
                first = False

            j = {
                "caption": "Tailwind Docs: {}".format(topic),
                "command": "tailwind_docs",
                "args": {"page": "{}".format(slug)}
            }
            json.dump(j, f)

    f.write('\n]\n')
