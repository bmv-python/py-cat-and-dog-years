from app.main import get_human_age


def test_check_that_before_15_years_age_is_0() -> None:
    assert (
        get_human_age(14, 14) == [0, 0]
    ), "check_that_before_15_years_age_is_0"


def test_check_that_15_years_age_is_1() -> None:
    assert (
        get_human_age(15, 15) == [1, 1]
    ), "check_that_15_years_age_is_1"


def test_check_that_before_24_years_age_is_1() -> None:
    assert (
        get_human_age(23, 23) == [1, 1]
    ), "check_that_before_24_years_age_is_1"


def test_check_that_24_years_age_is_2() -> None:
    assert (
        get_human_age(24, 24) == [2, 2]
    ), "check_that_24_years_age_is_2"


def test_years_calculation_after_24() -> None:
    assert (
        get_human_age(100, 100) == [21, 17]
    ), "years_calculation_after_24"
