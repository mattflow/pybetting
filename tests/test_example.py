from betting.example import get_greeting


def test_get_greeting():
    assert get_greeting() == "Hello world"
    assert get_greeting("python") == "Hello python"
