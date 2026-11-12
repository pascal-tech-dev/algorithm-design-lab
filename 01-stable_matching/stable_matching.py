"""
A matching is stable if there is no blocking pair (called unstable pair)
A blocking pair consists of a man m and a woman w who are not currently to each other, but:
    1. m prefers w over his current partner.
    2. w prefers m over her current partner.
"""

from operator import index


def is_stable_matching(
    men_pref: dict[str, list[str]],
    women_pref: dict[str, list[str]],
    matching: list[tuple[str, str]]
) -> bool:
    """
    Return True if the given perfect matching is stable.

    Assume: 
    - Both sides have the same number of participants.
    - Every preference list is a strict, complete rankings.
    - The matching is already a valid perfect matching.
    """

    man_to_woman = dict[str, str](matching)
    woman_to_man = {w: m for m, w in matching}

    # all pairs except matching
    unmatched_pairs = {
        (m, w) 
        for m in men_pref
        for w in women_pref
    } - set[tuple[str,str]](matching)
    
    # find a blocking pair if possible
    for unmatched_pair in unmatched_pairs:
        m = unmatched_pair[0]
        w = unmatched_pair[1]
        blocking_pairs = False, False
        if men_pref[m].index(w) < men_pref[m].index(man_to_woman[m]):
            blocking_pairs = True, blocking_pairs[1]
            print(f"{m} prefers the {w} over {man_to_woman[m]}")
        if women_pref[w].index(m) < women_pref[w].index(woman_to_man[w]):
            blocking_pairs = blocking_pairs[0], True
            print(f"{w} prefers the {m} over {woman_to_man[w]}")
        if blocking_pairs[0] and blocking_pairs[1]:
            return False

    return True


def is_stable_matching_improved(
    men_pref: dict[str, list[str]],
    women_pref: dict[str, list[str]],
    matching: list[tuple[str, str]],
) -> bool:
    """
    Return True if the given perfect matching is stable.

    Same assumptions as is_stable_matching.

    Improvements over is_stable_matching:
    - Uses rank maps for O(1) preference comparisons (no repeated list.index)
    - Only checks women each man prefers over his current partner
    - No print side effects
    - Avoids building the full set of unmatched pairs
    """
    man_to_woman = dict(matching)
    woman_to_man = {w: m for m, w in matching}

    women_rank = {
        w: {m: i for i, m in enumerate(prefs)}
        for w, prefs in women_pref.items()
    }

    for m, prefs in men_pref.items():
        current_w = man_to_woman[m]
        for w in prefs:
            # Pref lists are best-to-worst; stop once we reach the current partner.
            if w == current_w:
                break
            # m prefers w over his partner; blocking if w also prefers m over hers.
            her_man = woman_to_man[w]
            if women_rank[w][m] < women_rank[w][her_man]:
                return False

    return True


# For example: below is not stable
men_preferences = {
    "m1": ["w2", "w1", "w3"],
    "m2": ["w2", "w3", "w1"],
    "m3": ["w3", "w1", "w2"],
}

women_preferences = {
    "w1": ["m1", "m2", "m3"],
    "w2": ["m1", "m2", "m3"],
    "w3": ["m3", "m2", "m1"],
}

matching = [
    ("m1", "w1"),
    ("m2", "w2"),
    ("m3", "w3"),
]

assert is_stable_matching(
    men_preferences,
    women_preferences,
    matching,
) is False

assert is_stable_matching_improved(
    men_preferences,
    women_preferences,
    matching,
) is False

