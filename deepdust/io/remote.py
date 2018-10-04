import urllib.request

def fetch(url, localpath):

    text = urllib.request.urlopen(url).readlines()

    with open(localpath, mode='wb+') as f:
        for line in text:
            f.write(line)
