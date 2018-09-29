import json
import urllib

manifest_url_base = 'http://json-ld.org/test-suite/tests'

compaction_url = ('{}/compact-manifest.jsonld'
                           .format(manifest_url_base))

compaction_rawtext_dest = './compaction.jsonld'

def get_manifest(url, dest):
    latest_text = urllib.urlopen(url).readlines()

    with open(dest, mode='w') as f:
        for line in latest_text:
            f.write(line)
    

get_manifest(compaction_url, compaction_rawtext_dest)
