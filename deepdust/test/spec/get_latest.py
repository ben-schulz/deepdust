import json
import os

import jsonld
import remote


manifest_url_base = 'http://json-ld.org/test-suite/tests'

compaction_url = ('{}/compact-manifest.jsonld'
                           .format(manifest_url_base))

compaction_rawtext_dest = './compaction.jsonld'

remote.fetch(compaction_url, compaction_rawtext_dest)

cases = {}
with open(compaction_rawtext_dest, mode='rt') as f:

    rawtext = str.join('\n', f.readlines())
    cases = json.loads(rawtext)

c = jsonld.TestSuite(cases)

c.build_cases(remote.fetch)


this_module_path = os.path.abspath(__file__)
this_module_dir = os.path.dirname(this_module_path)
outfile = os.path.join(this_module_dir, 'test_foo.py')

with open(outfile, mode='wt') as f:
    f.write(str(c))
