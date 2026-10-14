"""
Exercise 6: build orderflow/password.py with TDD.

This file is almost empty on purpose. Unlike every other exercise here, the
production code does not exist yet, so you write the test first and let the
failing test tell you what to implement next.

The cycle, one rule at a time:

  1. RED      Write one test for one rule. Run it. It must fail, and it must
              fail for the reason you expect.
  2. GREEN    Write the smallest change to orderflow/password.py that makes
              it pass. Do not implement rules you have no test for yet.
  3. REFACTOR Tidy up the implementation with the suite green.

The rules and their exact error messages are in the README. Work down that
list in order, and commit after each green step so your history shows the
cycle.
"""

import pytest

from orderflow.password import validate_password


def test_password_shorter_than_eight_characters_is_rejected():
    """RED first: start here, with the length rule and nothing else."""
    # TODO: Call validate_password with a short password, e.g. "Ab1!"
    # TODO: Assert "Password must be at least 8 characters long" is in the result
    errors = validate_password("Ab1!")
    assert "Password must be at least 8 characters long" in errors


# TODO: Add one test per remaining rule from the README, in order:
# TODO:   uppercase, lowercase, digit, special character
# TODO: Then add a test that a fully valid password returns an empty list.
# TODO: Finally, add a test that a password breaking several rules at once
# TODO: reports every broken rule, not just the first.


def test_password_without_an_uppercase_letter_is_rejected():
    errors = validate_password("lowercase1!")
    assert "Password must contain an uppercase letter" in errors


def test_password_without_a_lowercase_letter_is_rejected():
    errors = validate_password("UPPERCASE1!")
    assert "Password must contain a lowercase letter" in errors


def test_password_without_a_digit_is_rejected():
    errors = validate_password("NoDigits!")
    assert "Password must contain a digit" in errors


def test_password_without_a_special_character_is_rejected():
    errors = validate_password("NoSpecial1")
    assert "Password must contain a special character" in errors


def test_valid_password_returns_no_errors():
    assert validate_password("ValidPass1!") == []


def test_password_with_multiple_broken_rules_reports_every_error():
    errors = validate_password("short")
    assert set(errors) == {
        "Password must be at least 8 characters long",
        "Password must contain an uppercase letter",
        "Password must contain a digit",
        "Password must contain a special character",
    }
