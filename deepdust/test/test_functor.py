import unittest

import deepdust.jsonld.functor as functor

class TestFunctor(unittest.TestCase):

    def test_apply_primitive_int(self):

        f = functor.Json(
            int_f=lambda x: x + 1
        )

        result = f.apply(2)

        self.assertEqual(result, 3)


    def test_apply_primitive_float(self):

        f = functor.Json(
            real_f=lambda x: x + 1
        )

        result = f.apply(2.7)

        self.assertEqual(result, 3.7)


    def test_apply_primitive_bool(self):

        f = functor.Json(
            bool_f=lambda x: not x
        )

        self.assertEqual(f.apply(True), False)
        self.assertEqual(f.apply(False), True)


    def test_apply_primitive_null(self):

        f = functor.Json(
            null_f=lambda x: 'null value'
        )

        self.assertEqual(f.apply(None), 'null value')


    def test_apply_primitive_string(self):

        f = functor.Json(
            string_f=lambda x: '"{}"'.format(x)
        )

        self.assertEqual('"x"', f.apply('x'))
        self.assertEqual('""', f.apply(''))
        self.assertEqual('"""', f.apply('"'))


    def test_apply_dictionary_flat(self):

        f = functor.Json(
            obj_f=(lambda a:
                   (lambda x: { k : (v*2)
                              for (k, v) in x.items()  }))
        )

        result = f.apply({'a':1, 'b':2, 'c':3})

        self.assertEqual(2, result['a'])
        self.assertEqual(4, result['b'])
        self.assertEqual(6, result['c'])


    def test_apply_array_flat(self):

        f = functor.Json(
            array_f=lambda a: (lambda x: [ y*3 for y in x ])
        )

        result = f.apply([1,2,3,4])

        self.assertEqual(3, result[0])
        self.assertEqual(6, result[1])
        self.assertEqual(9, result[2])
        self.assertEqual(12, result[3])


    def test_apply_dictionary_recursive_simple(self):

        f = functor.Json(
            obj_f=(lambda a:
                   (lambda x: { ('_' + k) : a(v)
                                for (k, v) in x.items() }))
        )

        result = f.apply({
            'a': { 'x' : 5, 'y' : 7  },
            'b': { 'u' : 4, 'v' : 6 }
        })

        self.assertEqual(result['_a']['_x'], 5)
        self.assertEqual(result['_a']['_y'], 7)
        self.assertEqual(result['_b']['_u'], 4)
        self.assertEqual(result['_b']['_v'], 6)


    def test_apply_array_recursive(self):

        def unify(x):
            if 1 == len(x):
                return x[0]
            return x

        f = functor.Json(
            array_f=lambda a: (lambda x: [ a(unify(y))
                                           for y in x ])
        )

        result = f.apply([
            ['a'],
            ['b', 'c'],
            ['d', 'e', 'f'],
            ['g'],
            ['h', 'i'],
            ['j']
        ])

        self.assertEqual('a', result[0])
        self.assertEqual(['b', 'c'], result[1])
        self.assertEqual(['d', 'e', 'f'], result[2])
        self.assertEqual('g', result[3])
        self.assertEqual(['h', 'i'], result[4])
        self.assertEqual('j', result[5])


    def test_heterogenous_types_recurse(self):

        renames = {
            'x': 'xx',
            'y': 'yy',
            'z': 'nothing'
        }

        f = functor.Json(
            obj_f=(lambda a:
                   (lambda x:
                    {renames[k] : a(v)
                     for (k, v) in x.items()})),
        )

        result = f.apply({
            'x' : [1, 2, 3],
            'y' : [4, 5, 6]
        })