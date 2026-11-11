def is_perfect_matching(
    men: set[str],
    women: set[str],
    matching: list[tuple[str, str]],
) -> bool:
    if len(matching) != len(men) or len(men) != len(women):
        return False

    matched_men = {man for man, _ in matching}
    matched_women = {woman for _, woman in matching}

    return (
        len(matched_men) == len(matching)
        and len(matched_women) == len(matching)
        and matched_men == men
        and matched_women == women
    )