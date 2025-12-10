def bin_to_dec(binarni_cislo):
    bin_str = str(binarni_cislo)
    bin_str = bin_str.lstrip("0")
    if bin_str == "":
        return 0
    return int(bin_str, 2)


def test_bin_to_dec():
    assert bin_to_dec("0") == 0
    assert bin_to_dec(1) == 1
    assert bin_to_dec("100") == 4
    assert bin_to_dec(101) == 5
    assert bin_to_dec("010101") == 21
    assert bin_to_dec(10000000) == 128

# volitelné spuštění testu
test_bin_to_dec()
