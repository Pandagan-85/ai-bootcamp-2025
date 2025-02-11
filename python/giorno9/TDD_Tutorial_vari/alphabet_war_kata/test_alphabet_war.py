import pytest
from alphabet_war import alphabet_war


def test_alphabet_war_cases_z_wins_right():
    result = alphabet_war("z")
    assert result == "Right side wins!"


def test_alphabet_war_cases_asterics_fights_again():
    assert (alphabet_war("****") == "Let's fight again!")


def test_alphabet_war_fight_again():
    assert (alphabet_war("z*dq*mw*pb*s") == "Let's fight again!")

def test_alphabet_war_fight_again_pareggio():
    assert (alphabet_war("zdqmwpbs") == "Let's fight again!")
def test_alphabet_war_right_wins():
    assert (alphabet_war("zz*zzs") == "Right side wins!")

def test_alphabet_war_left_wins():
    assert (alphabet_war("sz**z**zs") == "Left side wins!")
    assert (alphabet_war("z*z*z*zs") == "Left side wins!")
    assert (alphabet_war("*wwwwww*z*") == "Left side wins!")
def test_alphabet_war_fightt_again_bomb():
    assert (alphabet_war("w****z") == "Let's fight again!")
    assert (alphabet_war("mb**qwwp**dm") == "Let's fight again!")
