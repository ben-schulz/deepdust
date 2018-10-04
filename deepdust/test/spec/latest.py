import json
import os
import sys

import deepdust.test.spec.jsonld as jsonld

import deepdust.io.remote as remote
import deepdust.io.files as files

def build():

    manifest_url_base = 'http://json-ld.org/test-suite/tests'

    manifest_file = 'compact-manifest.jsonld'
    compaction_url = ('{}/{}'.format(manifest_url_base,
                                     manifest_file))

    artifact_dir = files.relative(__name__, 'cases')
    
    compaction_rawtext_dest = os.path.join(
        artifact_dir, manifest_file)

    files.clean_directory('test/spec/cases')
    remote.fetch(compaction_url, compaction_rawtext_dest)

    cases = {}
    with open(compaction_rawtext_dest, mode='rt') as f:

        rawtext = str.join('\n', f.readlines())
        cases = json.loads(rawtext)

    c = jsonld.TestSuite(cases)

    c.build_cases(remote.fetch)

    outfile = files.relative(__name__, 'test_compaction.py')

    with open(outfile, mode='wt') as f:
        f.write(str(c))

        
