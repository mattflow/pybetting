from betting.example import get_greeting, get_language


def test_get_greeting() -> None:
    assert get_greeting() == "Hello world"
    assert get_greeting("python") == "Hello python"


def test_get_language() -> None:
    assert get_language() == "python"
