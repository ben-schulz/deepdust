#generated: 2018-09-30 11:11:32.964492
import unittest
import json

import deepdust.jsonld.document
import deepdust.io.files

import deepdust.test.claim as claim


def load_json(filename):

    f = open(deepdust.io.files.relative(__name__, "cases/" + filename))
    obj = None
    try:
        obj = json.load(f)

    finally:
        f.close()

    return obj

class TestCompaction(unittest.TestCase):


        def test_drop_free_floating_nodes(self):

            case = load_json("compact-0001-in.jsonld")
            context = load_json("compact-0001-context.jsonld")
            expect = load_json("compact-0001-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_basic(self):

            case = load_json("compact-0002-in.jsonld")
            context = load_json("compact-0002-context.jsonld")
            expect = load_json("compact-0002-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_drop_null_and_unmapped_properties(self):

            case = load_json("compact-0003-in.jsonld")
            context = load_json("compact-0003-context.jsonld")
            expect = load_json("compact-0003-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_optimize___token_at__set_keep_empty_arrays(self):

            case = load_json("compact-0004-in.jsonld")
            context = load_json("compact-0004-context.jsonld")
            expect = load_json("compact-0004-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test___token_at__type_and_prefix_compaction(self):

            case = load_json("compact-0005-in.jsonld")
            context = load_json("compact-0005-context.jsonld")
            expect = load_json("compact-0005-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_keep_expanded_object_format_if___token_at__type_doesnt_match(self):

            case = load_json("compact-0006-in.jsonld")
            context = load_json("compact-0006-context.jsonld")
            expect = load_json("compact-0006-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_add_context(self):

            case = load_json("compact-0007-in.jsonld")
            context = load_json("compact-0007-context.jsonld")
            expect = load_json("compact-0007-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_alias_keywords(self):

            case = load_json("compact-0008-in.jsonld")
            context = load_json("compact-0008-context.jsonld")
            expect = load_json("compact-0008-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_compact___token_at__id(self):

            case = load_json("compact-0009-in.jsonld")
            context = load_json("compact-0009-context.jsonld")
            expect = load_json("compact-0009-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_array_to___token_at__graph(self):

            case = load_json("compact-0010-in.jsonld")
            context = load_json("compact-0010-context.jsonld")
            expect = load_json("compact-0010-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_compact_date(self):

            case = load_json("compact-0011-in.jsonld")
            context = load_json("compact-0011-context.jsonld")
            expect = load_json("compact-0011-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_native_types(self):

            case = load_json("compact-0012-in.jsonld")
            context = load_json("compact-0012-context.jsonld")
            expect = load_json("compact-0012-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test___token_at__value_with___token_at__language(self):

            case = load_json("compact-0013-in.jsonld")
            context = load_json("compact-0013-context.jsonld")
            expect = load_json("compact-0013-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_array_to_aliased___token_at__graph(self):

            case = load_json("compact-0014-in.jsonld")
            context = load_json("compact-0014-context.jsonld")
            expect = load_json("compact-0014-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_best_match_compaction(self):

            case = load_json("compact-0015-in.jsonld")
            context = load_json("compact-0015-context.jsonld")
            expect = load_json("compact-0015-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_recursive_named_graphs(self):

            case = load_json("compact-0016-in.jsonld")
            context = load_json("compact-0016-context.jsonld")
            expect = load_json("compact-0016-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_A_term_mapping_to_null_removes_the_mapping(self):

            case = load_json("compact-0017-in.jsonld")
            context = load_json("compact-0017-context.jsonld")
            expect = load_json("compact-0017-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_best_matching_term_for_lists(self):

            case = load_json("compact-0018-in.jsonld")
            context = load_json("compact-0018-context.jsonld")
            expect = load_json("compact-0018-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Keep_duplicate_values_in___token_at__list_and___token_at__set(self):

            case = load_json("compact-0019-in.jsonld")
            context = load_json("compact-0019-context.jsonld")
            expect = load_json("compact-0019-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Compact___token_at__id_that_is_a_property_IRI_when___token_at__container_is___token_at__list(self):

            case = load_json("compact-0020-in.jsonld")
            context = load_json("compact-0020-context.jsonld")
            expect = load_json("compact-0020-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Compact_properties_and_types_using___token_at__vocab(self):

            case = load_json("compact-0021-in.jsonld")
            context = load_json("compact-0021-context.jsonld")
            expect = load_json("compact-0021-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test___token_at__list_compaction_of_nested_properties(self):

            case = load_json("compact-0022-in.jsonld")
            context = load_json("compact-0022-context.jsonld")
            expect = load_json("compact-0022-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_prefer___token_at__vocab_over_compacted_IRIs(self):

            case = load_json("compact-0023-in.jsonld")
            context = load_json("compact-0023-context.jsonld")
            expect = load_json("compact-0023-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_most_specific_term_matching_in___token_at__list(self):

            case = load_json("compact-0024-in.jsonld")
            context = load_json("compact-0024-context.jsonld")
            expect = load_json("compact-0024-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Language_maps(self):

            case = load_json("compact-0025-in.jsonld")
            context = load_json("compact-0025-context.jsonld")
            expect = load_json("compact-0025-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Language_map_term_selection_with_complications(self):

            case = load_json("compact-0026-in.jsonld")
            context = load_json("compact-0026-context.jsonld")
            expect = load_json("compact-0026-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test___token_at__container__token__colon____token_at__set_with_multiple_values(self):

            case = load_json("compact-0027-in.jsonld")
            context = load_json("compact-0027-context.jsonld")
            expect = load_json("compact-0027-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Alias_keywords_and_use___token_at__vocab(self):

            case = load_json("compact-0028-in.jsonld")
            context = load_json("compact-0028-context.jsonld")
            expect = load_json("compact-0028-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Simple___token_at__index_map(self):

            case = load_json("compact-0029-in.jsonld")
            context = load_json("compact-0029-context.jsonld")
            expect = load_json("compact-0029-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_non_matching___token_at__container__token__colon____token_at__index(self):

            case = load_json("compact-0030-in.jsonld")
            context = load_json("compact-0030-context.jsonld")
            expect = load_json("compact-0030-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Compact___token_at__reverse(self):

            case = load_json("compact-0031-in.jsonld")
            context = load_json("compact-0031-context.jsonld")
            expect = load_json("compact-0031-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Compact_keys_in_reverse_maps(self):

            case = load_json("compact-0032-in.jsonld")
            context = load_json("compact-0032-context.jsonld")
            expect = load_json("compact-0032-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Compact_reverse_map_to_reverse_property(self):

            case = load_json("compact-0033-in.jsonld")
            context = load_json("compact-0033-context.jsonld")
            expect = load_json("compact-0033-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Skip_property_with___token_at__reverse_if_no_match(self):

            case = load_json("compact-0034-in.jsonld")
            context = load_json("compact-0034-context.jsonld")
            expect = load_json("compact-0034-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Compact___token_at__reverse_node_references_using_strings(self):

            case = load_json("compact-0035-in.jsonld")
            context = load_json("compact-0035-context.jsonld")
            expect = load_json("compact-0035-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Compact_reverse_properties_using_index_containers(self):

            case = load_json("compact-0036-in.jsonld")
            context = load_json("compact-0036-context.jsonld")
            expect = load_json("compact-0036-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Compact_keys_in___token_at__reverse_using___token_at__vocab(self):

            case = load_json("compact-0037-in.jsonld")
            context = load_json("compact-0037-context.jsonld")
            expect = load_json("compact-0037-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Index_map_round_tripping(self):

            case = load_json("compact-0038-in.jsonld")
            context = load_json("compact-0038-context.jsonld")
            expect = load_json("compact-0038-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Index_map_round_tripping(self):

            case = load_json("compact-0038-in.jsonld")
            context = load_json("compact-0038-context.jsonld")
            expect = load_json("compact-0038a-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test___token_at__graph_is_array(self):

            case = load_json("compact-0039-in.jsonld")
            context = load_json("compact-0039-context.jsonld")
            expect = load_json("compact-0039-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test___token_at__list_is_array(self):

            case = load_json("compact-0040-in.jsonld")
            context = load_json("compact-0040-context.jsonld")
            expect = load_json("compact-0040-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_index_rejects_term_having___token_at__list(self):

            case = load_json("compact-0041-in.jsonld")
            context = load_json("compact-0041-context.jsonld")
            expect = load_json("compact-0041-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test___token_at__list_keyword_aliasing(self):

            case = load_json("compact-0042-in.jsonld")
            context = load_json("compact-0042-context.jsonld")
            expect = load_json("compact-0042-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_select_term_over___token_at__vocab(self):

            case = load_json("compact-0043-in.jsonld")
            context = load_json("compact-0043-context.jsonld")
            expect = load_json("compact-0043-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test___token_at__type__token__colon____token_at__vocab_in_reverse_map(self):

            case = load_json("compact-0044-in.jsonld")
            context = load_json("compact-0044-context.jsonld")
            expect = load_json("compact-0044-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test___token_at__id_value_uses_relative_IRI_not_term(self):

            case = load_json("compact-0045-in.jsonld")
            context = load_json("compact-0045-context.jsonld")
            expect = load_json("compact-0045-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_multiple_objects_without___token_at__context_use___token_at__graph(self):

            case = load_json("compact-0046-in.jsonld")
            context = load_json("compact-0046-context.jsonld")
            expect = load_json("compact-0046-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Round_trip_relative_URLs(self):

            case = load_json("compact-0047-in.jsonld")
            context = load_json("compact-0047-context.jsonld")
            expect = load_json("compact-0047-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_term_with___token_at__language__token__colon__null(self):

            case = load_json("compact-0048-in.jsonld")
            context = load_json("compact-0048-context.jsonld")
            expect = load_json("compact-0048-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Round_tripping_of_lists_that_contain_just_IRIs(self):

            case = load_json("compact-0049-in.jsonld")
            context = load_json("compact-0049-context.jsonld")
            expect = load_json("compact-0049-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Reverse_properties_require___token_at__type__token__colon____token_at__id_to_use_string_values(self):

            case = load_json("compact-0050-in.jsonld")
            context = load_json("compact-0050-context.jsonld")
            expect = load_json("compact-0050-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Round_tripping___token_at__list_with_scalar(self):

            case = load_json("compact-0051-in.jsonld")
            context = load_json("compact-0051-context.jsonld")
            expect = load_json("compact-0051-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Round_tripping___token_at__list_with_scalar_and___token_at__graph_alias(self):

            case = load_json("compact-0052-in.jsonld")
            context = load_json("compact-0052-context.jsonld")
            expect = load_json("compact-0052-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Use___token_at__type__token__colon____token_at__vocab_if_no___token_at__type__token__colon____token_at__id(self):

            case = load_json("compact-0053-in.jsonld")
            context = load_json("compact-0053-context.jsonld")
            expect = load_json("compact-0053-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Compact_to___token_at__type__token__colon____token_at__vocab_and_compact___token_at__id_to_term(self):

            case = load_json("compact-0054-in.jsonld")
            context = load_json("compact-0054-context.jsonld")
            expect = load_json("compact-0054-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Round_tripping___token_at__type__token__colon____token_at__vocab(self):

            case = load_json("compact-0055-in.jsonld")
            context = load_json("compact-0055-context.jsonld")
            expect = load_json("compact-0055-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Prefer___token_at__type__token__colon____token_at__vocab_over___token_at__type__token__colon____token_at__id_for_terms(self):

            case = load_json("compact-0056-in.jsonld")
            context = load_json("compact-0056-context.jsonld")
            expect = load_json("compact-0056-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Complex_round_tripping___token_at__type__token__colon____token_at__vocab_and___token_at__type__token__colon____token_at__id(self):

            case = load_json("compact-0057-in.jsonld")
            context = load_json("compact-0057-context.jsonld")
            expect = load_json("compact-0057-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Prefer___token_at__type__token__colon____token_at__id_over___token_at__type__token__colon____token_at__vocab_for_non_terms(self):

            case = load_json("compact-0058-in.jsonld")
            context = load_json("compact-0058-context.jsonld")
            expect = load_json("compact-0058-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Term_with___token_at__type__token__colon____token_at__vocab_if_no___token_at__type__token__colon____token_at__id(self):

            case = load_json("compact-0059-in.jsonld")
            context = load_json("compact-0059-context.jsonld")
            expect = load_json("compact-0059-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Term_with___token_at__type__token__colon____token_at__id_if_no___token_at__type__token__colon____token_at__vocab_and_term_value(self):

            case = load_json("compact-0060-in.jsonld")
            context = load_json("compact-0060-context.jsonld")
            expect = load_json("compact-0060-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test___token_at__type__token__colon____token_at__vocab__token__fslash___token_at__id_with_values_matching_either(self):

            case = load_json("compact-0061-in.jsonld")
            context = load_json("compact-0061-context.jsonld")
            expect = load_json("compact-0061-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test___token_at__type__token__colon____token_at__vocab_and_relative_IRIs(self):

            case = load_json("compact-0062-in.jsonld")
            context = load_json("compact-0062-context.jsonld")
            expect = load_json("compact-0062-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Compact_IRI_round_tripping_with___token_at__type__token__colon____token_at__vocab(self):

            case = load_json("compact-0063-in.jsonld")
            context = load_json("compact-0063-context.jsonld")
            expect = load_json("compact-0063-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Compact_language_tagged_and_indexed_strings_to_index_map(self):

            case = load_json("compact-0064-in.jsonld")
            context = load_json("compact-0064-context.jsonld")
            expect = load_json("compact-0064-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Language_tagged_and_indexed_strings_with_language_map(self):

            case = load_json("compact-0065-in.jsonld")
            context = load_json("compact-0065-context.jsonld")
            expect = load_json("compact-0065-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Relative_IRIs(self):

            case = load_json("compact-0066-in.jsonld")
            context = load_json("compact-0066-context.jsonld")
            expect = load_json("compact-0066-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Reverse_properties_with_blank_nodes(self):

            case = load_json("compact-0067-in.jsonld")
            context = load_json("compact-0067-context.jsonld")
            expect = load_json("compact-0067-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Single_value_reverse_properties(self):

            case = load_json("compact-0068-in.jsonld")
            context = load_json("compact-0068-context.jsonld")
            expect = load_json("compact-0068-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Single_value_reverse_properties_with___token_at__set(self):

            case = load_json("compact-0069-in.jsonld")
            context = load_json("compact-0069-context.jsonld")
            expect = load_json("compact-0069-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_compactArrays_option(self):

            case = load_json("compact-0070-in.jsonld")
            context = load_json("compact-0070-context.jsonld")
            expect = load_json("compact-0070-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Input_has_multiple___token_at__contexts_output_has_one(self):

            case = load_json("compact-0071-in.jsonld")
            context = load_json("compact-0071-context.jsonld")
            expect = load_json("compact-0071-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Default_language_and_unmapped_properties(self):

            case = load_json("compact-0072-in.jsonld")
            context = load_json("compact-0072-context.jsonld")
            expect = load_json("compact-0072-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Mapped___token_at__id_and___token_at__type(self):

            case = load_json("compact-0073-in.jsonld")
            context = load_json("compact-0073-context.jsonld")
            expect = load_json("compact-0073-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Container_as_a_list_with_type_of___token_at__id(self):

            case = load_json("compact-0074-in.jsonld")
            context = load_json("compact-0074-context.jsonld")
            expect = load_json("compact-0074-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Compact_using_relative_fragment_identifier(self):

            case = load_json("compact-0075-in.jsonld")
            context = load_json("compact-0075-context.jsonld")
            expect = load_json("compact-0075-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Compacting_IRI_equivalent_to_base(self):

            case = load_json("compact-0076-in.jsonld")
            context = load_json("compact-0076-context.jsonld")
            expect = load_json("compact-0076-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Compact_a___token_at__graph_container(self):

            case = load_json("compact-0077-in.jsonld")
            context = load_json("compact-0077-context.jsonld")
            expect = load_json("compact-0077-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Compact_a___token__lbracket___token_at__graph___token_at__set__token__rbracket__container(self):

            case = load_json("compact-0078-in.jsonld")
            context = load_json("compact-0078-context.jsonld")
            expect = load_json("compact-0078-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Compact_a___token_at__graph_container_having___token_at__index(self):

            case = load_json("compact-0079-in.jsonld")
            context = load_json("compact-0079-context.jsonld")
            expect = load_json("compact-0079-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Do_not_compact_a_graph_having___token_at__id_with_a_term_having_an___token_at__graph_container(self):

            case = load_json("compact-0080-in.jsonld")
            context = load_json("compact-0080-context.jsonld")
            expect = load_json("compact-0080-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Compact_a___token__lbracket___token_at__graph___token_at__index__token__rbracket__container(self):

            case = load_json("compact-0081-in.jsonld")
            context = load_json("compact-0081-context.jsonld")
            expect = load_json("compact-0081-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Compact_a___token__lbracket___token_at__graph___token_at__index___token_at__set__token__rbracket__container(self):

            case = load_json("compact-0082-in.jsonld")
            context = load_json("compact-0082-context.jsonld")
            expect = load_json("compact-0082-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test___token__lbracket___token_at__graph___token_at__index__token__rbracket__does_not_compact_graph_with___token_at__id(self):

            case = load_json("compact-0083-in.jsonld")
            context = load_json("compact-0083-context.jsonld")
            expect = load_json("compact-0083-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Compact_a_simple_graph_with_a___token__lbracket___token_at__graph___token_at__id__token__rbracket__container(self):

            case = load_json("compact-0084-in.jsonld")
            context = load_json("compact-0084-context.jsonld")
            expect = load_json("compact-0084-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Compact_a_named_graph_with_a___token__lbracket___token_at__graph___token_at__id__token__rbracket__container(self):

            case = load_json("compact-0085-in.jsonld")
            context = load_json("compact-0085-context.jsonld")
            expect = load_json("compact-0085-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Compact_a_simple_graph_with_a___token__lbracket___token_at__graph___token_at__id___token_at__set__token__rbracket__container(self):

            case = load_json("compact-0086-in.jsonld")
            context = load_json("compact-0086-context.jsonld")
            expect = load_json("compact-0086-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Compact_a_named_graph_with_a___token__lbracket___token_at__graph___token_at__id___token_at__set__token__rbracket__container(self):

            case = load_json("compact-0087-in.jsonld")
            context = load_json("compact-0087-context.jsonld")
            expect = load_json("compact-0087-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Compact_a_graph_with___token_at__index_using_a___token__lbracket___token_at__graph___token_at__id__token__rbracket__container(self):

            case = load_json("compact-0088-in.jsonld")
            context = load_json("compact-0088-context.jsonld")
            expect = load_json("compact-0088-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Language_map_term_selection_with_complications(self):

            case = load_json("compact-0089-in.jsonld")
            context = load_json("compact-0089-context.jsonld")
            expect = load_json("compact-0089-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Compact_input_with___token_at__graph_container_to_output_without___token_at__graph_container(self):

            case = load_json("compact-0090-in.jsonld")
            context = load_json("compact-0090-context.jsonld")
            expect = load_json("compact-0090-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Compact_input_with___token_at__graph_container_to_output_without___token_at__graph_container_with_compactArrays_unset(self):

            case = load_json("compact-0091-in.jsonld")
            context = load_json("compact-0091-context.jsonld")
            expect = load_json("compact-0091-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Compact_input_with___token__lbracket___token_at__graph___token_at__set__token__rbracket__container_to_output_without___token__lbracket___token_at__graph___token_at__set__token__rbracket__container(self):

            case = load_json("compact-0092-in.jsonld")
            context = load_json("compact-0092-context.jsonld")
            expect = load_json("compact-0092-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Compact_input_with___token__lbracket___token_at__graph___token_at__set__token__rbracket__container_to_output_without___token__lbracket___token_at__graph___token_at__set__token__rbracket__container_with_compactArrays_unset(self):

            case = load_json("compact-0093-in.jsonld")
            context = load_json("compact-0093-context.jsonld")
            expect = load_json("compact-0093-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Compact_input_with___token__lbracket___token_at__graph___token_at__set__token__rbracket__container_to_output_without___token__lbracket___token_at__graph___token_at__set__token__rbracket__container(self):

            case = load_json("compact-0094-in.jsonld")
            context = load_json("compact-0094-context.jsonld")
            expect = load_json("compact-0094-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Relative_propererty_IRIs_with___token_at__vocab__token__colon__(self):

            case = load_json("compact-0095-in.jsonld")
            context = load_json("compact-0095-context.jsonld")
            expect = load_json("compact-0095-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Compact___token_at__graph_container___token__lparen_multiple_objects__token__rparen_(self):

            case = load_json("compact-0096-in.jsonld")
            context = load_json("compact-0096-context.jsonld")
            expect = load_json("compact-0096-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Compact___token__lbracket___token_at__graph___token_at__set__token__rbracket__container___token__lparen_multiple_objects__token__rparen_(self):

            case = load_json("compact-0097-in.jsonld")
            context = load_json("compact-0097-context.jsonld")
            expect = load_json("compact-0097-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Compact___token__lbracket___token_at__graph___token_at__index__token__rbracket__container___token__lparen_multiple_indexed_objects__token__rparen_(self):

            case = load_json("compact-0098-in.jsonld")
            context = load_json("compact-0098-context.jsonld")
            expect = load_json("compact-0098-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Compact___token__lbracket___token_at__graph___token_at__index___token_at__set__token__rbracket__container___token__lparen_multiple_indexed_objects__token__rparen_(self):

            case = load_json("compact-0099-in.jsonld")
            context = load_json("compact-0099-context.jsonld")
            expect = load_json("compact-0099-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Compact___token__lbracket___token_at__graph___token_at__id__token__rbracket__container___token__lparen_multiple_indexed_objects__token__rparen_(self):

            case = load_json("compact-0100-in.jsonld")
            context = load_json("compact-0100-context.jsonld")
            expect = load_json("compact-0100-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Compact___token__lbracket___token_at__graph___token_at__id___token_at__set__token__rbracket__container___token__lparen_multiple_indexed_objects__token__rparen_(self):

            case = load_json("compact-0101-in.jsonld")
            context = load_json("compact-0101-context.jsonld")
            expect = load_json("compact-0101-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Compact___token__lbracket___token_at__graph___token_at__index__token__rbracket__container___token__lparen_multiple_indexes_and_objects__token__rparen_(self):

            case = load_json("compact-0102-in.jsonld")
            context = load_json("compact-0102-context.jsonld")
            expect = load_json("compact-0102-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Compact___token__lbracket___token_at__graph___token_at__id__token__rbracket__container___token__lparen_multiple_ids_and_objects__token__rparen_(self):

            case = load_json("compact-0103-in.jsonld")
            context = load_json("compact-0103-context.jsonld")
            expect = load_json("compact-0103-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_adding_new_term(self):

            case = load_json("compact-c001-in.jsonld")
            context = load_json("compact-c001-context.jsonld")
            expect = load_json("compact-c001-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_overriding_a_term(self):

            case = load_json("compact-c002-in.jsonld")
            context = load_json("compact-c002-context.jsonld")
            expect = load_json("compact-c002-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_property_and_value_with_different_terms_mapping_to_the_same_expanded_property(self):

            case = load_json("compact-c003-in.jsonld")
            context = load_json("compact-c003-context.jsonld")
            expect = load_json("compact-c003-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_deep___token_at__context_affects_nested_nodes(self):

            case = load_json("compact-c004-in.jsonld")
            context = load_json("compact-c004-context.jsonld")
            expect = load_json("compact-c004-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_scoped_context_layers_on_intemediate_contexts(self):

            case = load_json("compact-c005-in.jsonld")
            context = load_json("compact-c005-context.jsonld")
            expect = load_json("compact-c005-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_adding_new_term(self):

            case = load_json("compact-c006-in.jsonld")
            context = load_json("compact-c006-context.jsonld")
            expect = load_json("compact-c006-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_overriding_a_term(self):

            case = load_json("compact-c007-in.jsonld")
            context = load_json("compact-c007-context.jsonld")
            expect = load_json("compact-c007-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_alias_of___token_at__type(self):

            case = load_json("compact-c008-in.jsonld")
            context = load_json("compact-c008-context.jsonld")
            expect = load_json("compact-c008-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_deep___token_at__context_affects_nested_nodes(self):

            case = load_json("compact-c009-in.jsonld")
            context = load_json("compact-c009-context.jsonld")
            expect = load_json("compact-c009-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_scoped_context_layers_on_intemediate_contexts(self):

            case = load_json("compact-c010-in.jsonld")
            context = load_json("compact-c010-context.jsonld")
            expect = load_json("compact-c010-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_applies_context_for_all_values(self):

            case = load_json("compact-c011-in.jsonld")
            context = load_json("compact-c011-context.jsonld")
            expect = load_json("compact-c011-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_orders___token_at__type_terms_when_applying_scoped_contexts(self):

            case = load_json("compact-c012-in.jsonld")
            context = load_json("compact-c012-context.jsonld")
            expect = load_json("compact-c012-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Indexes_to_object_not_having_an___token_at__id(self):

            case = load_json("compact-m001-in.jsonld")
            context = load_json("compact-m001-context.jsonld")
            expect = load_json("compact-m001-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Indexes_to_object_already_having_an___token_at__id(self):

            case = load_json("compact-m002-in.jsonld")
            context = load_json("compact-m002-context.jsonld")
            expect = load_json("compact-m002-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Indexes_to_object_not_having_an___token_at__type(self):

            case = load_json("compact-m003-in.jsonld")
            context = load_json("compact-m003-context.jsonld")
            expect = load_json("compact-m003-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Indexes_to_object_already_having_an___token_at__type(self):

            case = load_json("compact-m004-in.jsonld")
            context = load_json("compact-m004-context.jsonld")
            expect = load_json("compact-m004-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Indexes_to_object_using_compact_IRI___token_at__id(self):

            case = load_json("compact-m005-in.jsonld")
            context = load_json("compact-m005-context.jsonld")
            expect = load_json("compact-m005-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Indexes_using_compacted___token_at__type(self):

            case = load_json("compact-m006-in.jsonld")
            context = load_json("compact-m006-context.jsonld")
            expect = load_json("compact-m006-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_When_type_is_in_a_type_map(self):

            case = load_json("compact-m007-in.jsonld")
            context = load_json("compact-m007-context.jsonld")
            expect = load_json("compact-m007-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test___token_at__index_map_with___token_at__none_node_definition(self):

            case = load_json("compact-m008-in.jsonld")
            context = load_json("compact-m008-context.jsonld")
            expect = load_json("compact-m008-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test___token_at__index_map_with___token_at__none_value(self):

            case = load_json("compact-m009-in.jsonld")
            context = load_json("compact-m009-context.jsonld")
            expect = load_json("compact-m009-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test___token_at__index_map_with___token_at__none_value_using_alias_of___token_at__none(self):

            case = load_json("compact-m010-in.jsonld")
            context = load_json("compact-m010-context.jsonld")
            expect = load_json("compact-m010-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test___token_at__language_map_with_no___token_at__language(self):

            case = load_json("compact-m011-in.jsonld")
            context = load_json("compact-m011-context.jsonld")
            expect = load_json("compact-m011-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_language_map_with_no___token_at__language_using_alias_of___token_at__none(self):

            case = load_json("compact-m012-in.jsonld")
            context = load_json("compact-m012-context.jsonld")
            expect = load_json("compact-m012-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_id_map_using___token_at__none(self):

            case = load_json("compact-m013-in.jsonld")
            context = load_json("compact-m013-context.jsonld")
            expect = load_json("compact-m013-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_id_map_using___token_at__none_with_alias(self):

            case = load_json("compact-m014-in.jsonld")
            context = load_json("compact-m014-context.jsonld")
            expect = load_json("compact-m014-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_type_map_using___token_at__none_with_alias(self):

            case = load_json("compact-m015-in.jsonld")
            context = load_json("compact-m015-context.jsonld")
            expect = load_json("compact-m015-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_type_map_using___token_at__none_with_alias(self):

            case = load_json("compact-m016-in.jsonld")
            context = load_json("compact-m016-context.jsonld")
            expect = load_json("compact-m016-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_graph_index_map_using___token_at__none(self):

            case = load_json("compact-m017-in.jsonld")
            context = load_json("compact-m017-context.jsonld")
            expect = load_json("compact-m017-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_graph_id_map_using___token_at__none(self):

            case = load_json("compact-m018-in.jsonld")
            context = load_json("compact-m018-context.jsonld")
            expect = load_json("compact-m018-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_graph_id_map_using_alias_of___token_at__none(self):

            case = load_json("compact-m019-in.jsonld")
            context = load_json("compact-m019-context.jsonld")
            expect = load_json("compact-m019-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Indexes_to___token_at__nest_for_property_with___token_at__nest(self):

            case = load_json("compact-n001-in.jsonld")
            context = load_json("compact-n001-context.jsonld")
            expect = load_json("compact-n001-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Indexes_to___token_at__nest_for_all_properties_with___token_at__nest(self):

            case = load_json("compact-n002-in.jsonld")
            context = load_json("compact-n002-context.jsonld")
            expect = load_json("compact-n002-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Nests_using_alias_of___token_at__nest(self):

            case = load_json("compact-n003-in.jsonld")
            context = load_json("compact-n003-context.jsonld")
            expect = load_json("compact-n003-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Arrays_of_nested_values(self):

            case = load_json("compact-n004-in.jsonld")
            context = load_json("compact-n004-context.jsonld")
            expect = load_json("compact-n004-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Nested___token_at__container__token__colon____token_at__list(self):

            case = load_json("compact-n005-in.jsonld")
            context = load_json("compact-n005-context.jsonld")
            expect = load_json("compact-n005-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Nested___token_at__container__token__colon____token_at__index(self):

            case = load_json("compact-n006-in.jsonld")
            context = load_json("compact-n006-context.jsonld")
            expect = load_json("compact-n006-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Nested___token_at__container__token__colon____token_at__language(self):

            case = load_json("compact-n007-in.jsonld")
            context = load_json("compact-n007-context.jsonld")
            expect = load_json("compact-n007-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Nested___token_at__container__token__colon____token_at__type(self):

            case = load_json("compact-n008-in.jsonld")
            context = load_json("compact-n008-context.jsonld")
            expect = load_json("compact-n008-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Nested___token_at__container__token__colon____token_at__id(self):

            case = load_json("compact-n009-in.jsonld")
            context = load_json("compact-n009-context.jsonld")
            expect = load_json("compact-n009-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Multiple_nest_aliases(self):

            case = load_json("compact-n010-in.jsonld")
            context = load_json("compact-n010-context.jsonld")
            expect = load_json("compact-n010-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Compact_IRI_will_not_use_an_expanded_term_definition_in_10(self):

            case = load_json("compact-p001-in.jsonld")
            context = load_json("compact-p001-context.jsonld")
            expect = load_json("compact-p001-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Compact_IRI_does_not_use_expanded_term_definition_in_11(self):

            case = load_json("compact-p002-in.jsonld")
            context = load_json("compact-p002-context.jsonld")
            expect = load_json("compact-p002-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Compact_IRI_does_not_use_simple_term_that_does_not_end_with_a_gen_delim(self):

            case = load_json("compact-p003-in.jsonld")
            context = load_json("compact-p003-context.jsonld")
            expect = load_json("compact-p003-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Compact_IRIs_using_simple_terms_ending_with_gen_delim(self):

            case = load_json("compact-p004-in.jsonld")
            context = load_json("compact-p004-context.jsonld")
            expect = load_json("compact-p004-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Compact_IRI_uses_term_with_definition_including___token_at__prefix__token__colon__true(self):

            case = load_json("compact-p005-in.jsonld")
            context = load_json("compact-p005-context.jsonld")
            expect = load_json("compact-p005-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Compact_IRI_uses_term_with_definition_including___token_at__prefix__token__colon__true(self):

            case = load_json("compact-p006-in.jsonld")
            context = load_json("compact-p006-context.jsonld")
            expect = load_json("compact-p006-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Compact_IRI_not_used_as_prefix(self):

            case = load_json("compact-p007-in.jsonld")
            context = load_json("compact-p007-context.jsonld")
            expect = load_json("compact-p007-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Compact_IRI_does_not_use_term_with_definition_including___token_at__prefix__token__colon__false(self):

            case = load_json("compact-p008-in.jsonld")
            context = load_json("compact-p008-context.jsonld")
            expect = load_json("compact-p008-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Expands_and_compacts_to_document_base_by_default(self):

            case = load_json("compact-r001-in.jsonld")
            context = load_json("compact-r001-context.jsonld")
            expect = load_json("compact-r001-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test_Expands_and_does_not_compact_to_document_base_with_compactToRelative_false(self):

            case = load_json("compact-r002-in.jsonld")
            context = load_json("compact-r002-context.jsonld")
            expect = load_json("compact-r002-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test___token_at__context_with_single_array_values(self):

            case = load_json("compact-s001-in.jsonld")
            context = load_json("compact-s001-context.jsonld")
            expect = load_json("compact-s001-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            


        def test___token_at__context_with_array_including___token_at__set_uses_array_values(self):

            case = load_json("compact-s002-in.jsonld")
            context = load_json("compact-s002-context.jsonld")
            expect = load_json("compact-s002-out.jsonld")

            result = deepdust.jsonld.document.compact(case, context)

            claim.Json.equal(expect, result)
            
