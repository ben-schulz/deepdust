
import unittest
import json

import deepdust.jsonld.document
import deepdust.test.claim as claim

class TestCompaction(unittest.TestCase):


        def test_drop_free_floating_nodes(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0001-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0001-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0001-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_basic(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0002-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0002-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0002-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_drop_null_and_unmapped_properties(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0003-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0003-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0003-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_optimize_@set,_keep_empty_arrays(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0004-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0004-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0004-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_@type_and_prefix_compaction(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0005-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0005-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0005-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_keep_expanded_object_format_if_@type_doesn't_match(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0006-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0006-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0006-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_add_context(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0007-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0007-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0007-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_alias_keywords(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0008-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0008-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0008-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_compact_@id(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0009-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0009-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0009-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_array_to_@graph(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0010-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0010-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0010-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_compact_date(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0011-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0011-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0011-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_native_types(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0012-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0012-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0012-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_@value_with_@language(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0013-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0013-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0013-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_array_to_aliased_@graph(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0014-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0014-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0014-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_best_match_compaction(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0015-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0015-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0015-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_recursive_named_graphs(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0016-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0016-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0016-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_A_term_mapping_to_null_removes_the_mapping(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0017-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0017-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0017-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_best_matching_term_for_lists(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0018-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0018-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0018-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Keep_duplicate_values_in_@list_and_@set(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0019-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0019-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0019-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Compact_@id_that_is_a_property_IRI_when_@container_is_@list(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0020-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0020-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0020-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Compact_properties_and_types_using_@vocab(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0021-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0021-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0021-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_@list_compaction_of_nested_properties(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0022-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0022-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0022-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_prefer_@vocab_over_compacted_IRIs(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0023-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0023-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0023-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_most_specific_term_matching_in_@list.(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0024-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0024-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0024-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Language_maps(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0025-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0025-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0025-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Language_map_term_selection_with_complications(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0026-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0026-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0026-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_@container:_@set_with_multiple_values(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0027-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0027-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0027-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Alias_keywords_and_use_@vocab(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0028-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0028-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0028-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Simple_@index_map(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0029-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0029-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0029-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_non_matching_@container:_@index(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0030-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0030-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0030-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Compact_@reverse(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0031-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0031-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0031-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Compact_keys_in_reverse_maps(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0032-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0032-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0032-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Compact_reverse_map_to_reverse_property(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0033-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0033-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0033-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Skip_property_with_@reverse_if_no_match(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0034-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0034-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0034-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Compact_@reverse_node_references_using_strings(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0035-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0035-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0035-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Compact_reverse_properties_using_index_containers(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0036-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0036-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0036-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Compact_keys_in_@reverse_using_@vocab(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0037-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0037-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0037-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Index_map_round_tripping(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0038-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0038-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0038-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Index_map_round_tripping(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0038-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0038a-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0038-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_@graph_is_array(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0039-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0039-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0039-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_@list_is_array(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0040-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0040-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0040-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_index_rejects_term_having_@list(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0041-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0041-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0041-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_@list_keyword_aliasing(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0042-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0042-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0042-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_select_term_over_@vocab(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0043-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0043-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0043-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_@type:_@vocab_in_reverse_map(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0044-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0044-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0044-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_@id_value_uses_relative_IRI,_not_term(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0045-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0045-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0045-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_multiple_objects_without_@context_use_@graph(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0046-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0046-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0046-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Round_trip_relative_URLs(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0047-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0047-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0047-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_term_with_@language:_null(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0048-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0048-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0048-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Round_tripping_of_lists_that_contain_just_IRIs(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0049-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0049-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0049-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Reverse_properties_require_@type:_@id_to_use_string_values(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0050-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0050-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0050-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Round_tripping_@list_with_scalar(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0051-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0051-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0051-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Round_tripping_@list_with_scalar_and_@graph_alias(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0052-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0052-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0052-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Use_@type:_@vocab_if_no_@type:_@id(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0053-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0053-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0053-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Compact_to_@type:_@vocab_and_compact_@id_to_term(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0054-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0054-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0054-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Round_tripping_@type:_@vocab(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0055-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0055-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0055-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Prefer_@type:_@vocab_over_@type:_@id_for_terms(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0056-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0056-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0056-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Complex_round_tripping_@type:_@vocab_and_@type:_@id(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0057-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0057-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0057-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Prefer_@type:_@id_over_@type:_@vocab_for_non_terms(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0058-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0058-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0058-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Term_with_@type:_@vocab_if_no_@type:_@id(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0059-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0059-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0059-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Term_with_@type:_@id_if_no_@type:_@vocab_and_term_value(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0060-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0060-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0060-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_@type:_@vocab/@id_with_values_matching_either(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0061-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0061-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0061-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_@type:_@vocab_and_relative_IRIs(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0062-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0062-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0062-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Compact_IRI_round_tripping_with_@type:_@vocab(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0063-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0063-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0063-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Compact_language_tagged_and_indexed_strings_to_index_map(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0064-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0064-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0064-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Language_tagged_and_indexed_strings_with_language_map(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0065-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0065-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0065-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Relative_IRIs(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0066-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0066-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0066-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Reverse_properties_with_blank_nodes(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0067-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0067-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0067-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Single_value_reverse_properties(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0068-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0068-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0068-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Single_value_reverse_properties_with_@set(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0069-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0069-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0069-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_compactArrays_option(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0070-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0070-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0070-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Input_has_multiple_@contexts,_output_has_one(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0071-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0071-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0071-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Default_language_and_unmapped_properties(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0072-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0072-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0072-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Mapped_@id_and_@type(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0073-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0073-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0073-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Container_as_a_list_with_type_of_@id(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0074-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0074-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0074-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Compact_using_relative_fragment_identifier(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0075-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0075-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0075-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Compacting_IRI_equivalent_to_base(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0076-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0076-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0076-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Compact_a_@graph_container(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0077-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0077-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0077-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Compact_a_[@graph,_@set]_container(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0078-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0078-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0078-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Compact_a_@graph_container_having_@index(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0079-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0079-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0079-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Do_not_compact_a_graph_having_@id_with_a_term_having_an_@graph_container(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0080-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0080-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0080-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Compact_a_[@graph,_@index]_container(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0081-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0081-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0081-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Compact_a_[@graph,_@index,_@set]_container(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0082-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0082-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0082-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_[@graph,_@index]_does_not_compact_graph_with_@id(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0083-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0083-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0083-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Compact_a_simple_graph_with_a_[@graph,_@id]_container(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0084-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0084-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0084-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Compact_a_named_graph_with_a_[@graph,_@id]_container(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0085-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0085-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0085-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Compact_a_simple_graph_with_a_[@graph,_@id,_@set]_container(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0086-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0086-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0086-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Compact_a_named_graph_with_a_[@graph,_@id,_@set]_container(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0087-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0087-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0087-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Compact_a_graph_with_@index_using_a_[@graph,_@id]_container(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0088-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0088-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0088-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Language_map_term_selection_with_complications(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0089-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0089-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0089-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Compact_input_with_@graph_container_to_output_without_@graph_container(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0090-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0090-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0090-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Compact_input_with_@graph_container_to_output_without_@graph_container_with_compactArrays_unset(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0091-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0091-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0091-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Compact_input_with_[@graph,_@set]_container_to_output_without_[@graph,_@set]_container(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0092-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0092-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0092-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Compact_input_with_[@graph,_@set]_container_to_output_without_[@graph,_@set]_container_with_compactArrays_unset(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0093-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0093-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0093-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Compact_input_with_[@graph,_@set]_container_to_output_without_[@graph,_@set]_container(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0094-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0094-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0094-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Relative_propererty_IRIs_with_@vocab:_''(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0095-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0095-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0095-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Compact_@graph_container_(multiple_objects)(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0096-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0096-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0096-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Compact_[@graph,_@set]_container_(multiple_objects)(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0097-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0097-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0097-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Compact_[@graph,_@index]_container_(multiple_indexed_objects)(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0098-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0098-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0098-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Compact_[@graph,_@index,_@set]_container_(multiple_indexed_objects)(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0099-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0099-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0099-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Compact_[@graph,_@id]_container_(multiple_indexed_objects)(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0100-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0100-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0100-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Compact_[@graph,_@id,_@set]_container_(multiple_indexed_objects)(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0101-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0101-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0101-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Compact_[@graph,_@index]_container_(multiple_indexes_and_objects)(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0102-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0102-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0102-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Compact_[@graph,_@id]_container_(multiple_ids_and_objects)(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0103-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0103-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-0103-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_adding_new_term(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-c001-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-c001-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-c001-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_overriding_a_term(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-c002-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-c002-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-c002-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_property_and_value_with_different_terms_mapping_to_the_same_expanded_property(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-c003-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-c003-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-c003-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_deep_@context_affects_nested_nodes(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-c004-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-c004-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-c004-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_scoped_context_layers_on_intemediate_contexts(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-c005-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-c005-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-c005-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_adding_new_term(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-c006-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-c006-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-c006-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_overriding_a_term(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-c007-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-c007-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-c007-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_alias_of_@type(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-c008-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-c008-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-c008-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_deep_@context_affects_nested_nodes(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-c009-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-c009-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-c009-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_scoped_context_layers_on_intemediate_contexts(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-c010-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-c010-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-c010-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_applies_context_for_all_values(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-c011-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-c011-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-c011-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_orders_@type_terms_when_applying_scoped_contexts(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-c012-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-c012-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-c012-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Indexes_to_object_not_having_an_@id(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-m001-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-m001-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-m001-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Indexes_to_object_already_having_an_@id(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-m002-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-m002-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-m002-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Indexes_to_object_not_having_an_@type(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-m003-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-m003-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-m003-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Indexes_to_object_already_having_an_@type(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-m004-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-m004-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-m004-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Indexes_to_object_using_compact_IRI_@id(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-m005-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-m005-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-m005-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Indexes_using_compacted_@type(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-m006-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-m006-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-m006-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_When_type_is_in_a_type_map(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-m007-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-m007-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-m007-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_@index_map_with_@none_node_definition(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-m008-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-m008-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-m008-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_@index_map_with_@none_value(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-m009-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-m009-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-m009-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_@index_map_with_@none_value_using_alias_of_@none(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-m010-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-m010-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-m010-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_@language_map_with_no_@language(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-m011-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-m011-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-m011-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_language_map_with_no_@language_using_alias_of_@none(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-m012-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-m012-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-m012-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_id_map_using_@none(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-m013-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-m013-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-m013-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_id_map_using_@none_with_alias(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-m014-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-m014-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-m014-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_type_map_using_@none_with_alias(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-m015-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-m015-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-m015-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_type_map_using_@none_with_alias(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-m016-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-m016-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-m016-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_graph_index_map_using_@none(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-m017-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-m017-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-m017-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_graph_id_map_using_@none(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-m018-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-m018-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-m018-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_graph_id_map_using_alias_of_@none(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-m019-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-m019-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-m019-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Indexes_to_@nest_for_property_with_@nest(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-n001-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-n001-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-n001-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Indexes_to_@nest_for_all_properties_with_@nest(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-n002-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-n002-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-n002-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Nests_using_alias_of_@nest(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-n003-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-n003-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-n003-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Arrays_of_nested_values(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-n004-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-n004-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-n004-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Nested_@container:_@list(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-n005-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-n005-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-n005-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Nested_@container:_@index(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-n006-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-n006-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-n006-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Nested_@container:_@language(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-n007-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-n007-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-n007-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Nested_@container:_@type(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-n008-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-n008-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-n008-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Nested_@container:_@id(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-n009-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-n009-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-n009-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Multiple_nest_aliases(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-n010-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-n010-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-n010-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Compact_IRI_will_not_use_an_expanded_term_definition_in_1.0(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-p001-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-p001-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-p001-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Compact_IRI_does_not_use_expanded_term_definition_in_1.1(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-p002-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-p002-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-p002-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Compact_IRI_does_not_use_simple_term_that_does_not_end_with_a_gen_delim(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-p003-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-p003-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-p003-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Compact_IRIs_using_simple_terms_ending_with_gen_delim(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-p004-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-p004-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-p004-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Compact_IRI_uses_term_with_definition_including_@prefix:_true(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-p005-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-p005-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-p005-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Compact_IRI_uses_term_with_definition_including_@prefix:_true(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-p006-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-p006-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-p006-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Compact_IRI_not_used_as_prefix(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-p007-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-p007-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-p007-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Compact_IRI_does_not_use_term_with_definition_including_@prefix:_false(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-p008-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-p008-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-p008-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Expands_and_compacts_to_document_base_by_default(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-r001-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-r001-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-r001-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Expands_and_does_not_compact_to_document_base_with_compactToRelative_false(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-r002-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-r002-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-r002-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_@context_with_single_array_values(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-s001-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-s001-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-s001-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_@context_with_array_including_@set_uses_array_values(self):

            case = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-s002-in.jsonld"))
            expect = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-s002-out.jsonld"))
            context = json.load(open("/home/slowpoke/sandbox/deepdust/deepdust/test/spec/cases/compact-s002-context.jsonld"))

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            
