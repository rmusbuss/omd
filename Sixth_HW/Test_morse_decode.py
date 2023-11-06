from morse_decode import decode
import pytest


@pytest.mark.parametrize(
    'source_string, result',
    [
        (decode('... --- ...'), 'SOS'),
        (decode(' ... .--. -.-. . '), 'SPCE'),
        (decode('.--. -.-- - .... --- -.'), 'PYTHON'),
        (decode('..--- ----- ..--- ....-'),
         '2024')
    ]
)
def test_decode(source_string, result):
    assert source_string == result


if __name__ == '__main__':
    pass
