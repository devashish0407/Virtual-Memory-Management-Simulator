from utils.input_parser import parse_reference_string


def test_parse_reference_string_accepts_hex_decimal_and_operations():
    parsed = parse_reference_string("0x10 R, 32 W, 0X2A r")

    assert parsed == [(16, "R"), (32, "W"), (42, "R")]


def test_parse_reference_string_skips_invalid_entries():
    parsed = parse_reference_string("0x10 R, bad, 16 X, 24 W")

    assert parsed == [(16, "R"), (24, "W")]

