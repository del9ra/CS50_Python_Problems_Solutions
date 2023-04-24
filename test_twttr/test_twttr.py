from twttr import shorten
def test_shorten():
    assert shorten("twitter") == "twttr"
def test_love():
    assert shorten("LOVE")== "LV"
def test_punc():
    assert shorten("CS!")== "CS!"
def test_number():
    assert shorten("LOV1")== "LV1"