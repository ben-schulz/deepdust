# deepdust

[![Build Status](https://travis-ci.org/ben-schulz/deepdust.svg?branch=master)](https://travis-ci.org/ben-schulz/deepdust)

## Getting Started

clone the repository, and in the top-level directory run:

```
python setup.py spec
```

to build python-executable source from the current [JSON-LD Test Suite](https://json-ld.org/test-suite/).

to run all currently implemented test cases:

```
python setup.py test
```

to develop on a specification feature, add its `@id` (without the `#`) to the [list of implemented cases](./deepdust/test/spec/implemented.py), so that the corresponding case will run on `test`.

(2018.10.04)
