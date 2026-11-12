import importlib.util
from pathlib import Path

import pytest

_path = Path(__file__).with_name("02-stable_matching.py")
_spec = importlib.util.spec_from_file_location("stable_matching_02", _path)
assert _spec is not None and _spec.loader is not None
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)

is_stable_matching = _mod.is_stable_matching
is_stable_matching_improved = _mod.is_stable_matching_improved

STABLE_CHECKERS = pytest.mark.parametrize(
    "checker",
    [is_stable_matching, is_stable_matching_improved],
    ids=["original", "improved"],
)


MEN_PREF = {
    "m1": ["w2", "w1", "w3"],
    "m2": ["w2", "w3", "w1"],
    "m3": ["w3", "w1", "w2"],
}

WOMEN_PREF = {
    "w1": ["m1", "m2", "m3"],
    "w2": ["m1", "m2", "m3"],
    "w3": ["m3", "m2", "m1"],
}


@STABLE_CHECKERS
def test_unstable_matching_has_blocking_pair(checker):
    matching = [
        ("m1", "w1"),
        ("m2", "w2"),
        ("m3", "w3"),
    ]
    assert checker(MEN_PREF, WOMEN_PREF, matching) is False


@STABLE_CHECKERS
def test_man_optimal_gale_shapley_matching_is_stable(checker):
    # Man-proposing Gale-Shapley result for the preferences above.
    matching = [
        ("m1", "w2"),
        ("m2", "w1"),
        ("m3", "w3"),
    ]
    assert checker(MEN_PREF, WOMEN_PREF, matching) is True


@STABLE_CHECKERS
def test_single_pair_is_stable(checker):
    men_pref = {"m1": ["w1"]}
    women_pref = {"w1": ["m1"]}
    matching = [("m1", "w1")]
    assert checker(men_pref, women_pref, matching) is True


@STABLE_CHECKERS
def test_two_pair_mutual_top_choice_is_stable(checker):
    men_pref = {
        "m1": ["w1", "w2"],
        "m2": ["w2", "w1"],
    }
    women_pref = {
        "w1": ["m1", "m2"],
        "w2": ["m2", "m1"],
    }
    matching = [("m1", "w1"), ("m2", "w2")]
    assert checker(men_pref, women_pref, matching) is True


@STABLE_CHECKERS
def test_two_pair_crossed_matching_is_unstable(checker):
    men_pref = {
        "m1": ["w1", "w2"],
        "m2": ["w2", "w1"],
    }
    women_pref = {
        "w1": ["m1", "m2"],
        "w2": ["m2", "m1"],
    }
    # Both prefer their other partner -> blocking pairs.
    matching = [("m1", "w2"), ("m2", "w1")]
    assert checker(men_pref, women_pref, matching) is False
