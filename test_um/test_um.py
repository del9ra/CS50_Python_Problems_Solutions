from um import count
def test_one():
    assert count("um") == 1

def test_punctuation():
    assert count("um, yes, um, no") == 2
    assert count("um: hello, um no, um") == 3
    assert count("um...") == 1
    assert count(",um}") == 1

def test_part_of_word():
    assert count("instrument") == 0
    assert count("pneumonia") == 0
    assert count("human") == 0

def test_case():
    assert count("Um, it's me") == 1
    assert count("i love UM you") == 1
