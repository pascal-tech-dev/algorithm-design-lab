from itertools import permutations

from stable_matching import is_stable_matching


def find_all_stable_matchings(
    men_preferences: dict[str, list[str]],
    women_preferences: dict[str, list[str]],
) -> list[list[tuple[str, str]]]:
    """
    Return all stable perfect matchings.

    Assume:
    - Both sides have n participants.
    - All preference lists are strict and complete.
    """
    men = list(men_preferences.keys())
    women = list(women_preferences.keys())

    stable_matchings = []
    for arrangement in permutations(women):
        matching = list(zip(men, arrangement))
        if is_stable_matching(men_preferences, women_preferences, matching):
            stable_matchings.append(matching)
    
    return stable_matchings


men_preferences = {
    "m1": ["w1", "w2", "w3"],
    "m2": ["w2", "w1", "w3"],
    "m3": ["w1", "w3", "w2"],
}

women_preferences = {
    "w1": ["m3", "m1", "m2"],
    "w2": ["m1", "m2", "m3"],
    "w3": ["m1", "m2", "m3"],
}

result = find_all_stable_matchings(
    men_preferences,
    women_preferences,
)

print(result)

men_preferences1 = {
    "m1": ["w1", "w2", "w3"],
    "m2": ["w2", "w1", "w3"],
    "m3": ["w3", "w1", "w2"],
}

women_preferences2 = {
    "w1": ["m2", "m1", "m3"],
    "w2": ["m1", "m2", "m3"],
    "w3": ["m3", "m1", "m2"],
}

result2 = find_all_stable_matchings(
    men_preferences1,
    women_preferences2,
)

print(result2)