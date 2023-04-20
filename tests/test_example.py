from betting.example import get_greeting


def test_get_greeting() -> None:
    assert get_greeting() == "Hello world"
    assert get_greeting("python") == "Hello python"
