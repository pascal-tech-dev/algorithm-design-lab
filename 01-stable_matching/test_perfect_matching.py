from perfect_matching import is_perfect_matching


def test_valid_perfect_matching():
    men = {"a", "b"}
    women = {"x", "y"}
    matching = [("a", "x"), ("b", "y")]
    assert is_perfect_matching(men, women, matching) is True


def test_duplicate_man():
    men = {"a", "b"}
    women = {"x", "y"}
    matching = [("a", "x"), ("a", "y")]
    assert is_perfect_matching(men, women, matching) is False


def test_wrong_length():
    men = {"a", "b"}
    women = {"x", "y"}
    matching = [("a", "x")]
    assert is_perfect_matching(men, women, matching) is False