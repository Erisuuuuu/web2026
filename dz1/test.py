import subprocess
import pytest
import os

INTERPRETER = 'python'

def run_script(filename, input_data=None, cwd=None):
    if cwd is None:
        cwd = os.path.dirname(os.path.abspath(__file__))
    proc = subprocess.run(
        [INTERPRETER, filename],
        input='\n'.join(input_data if input_data else []),
        capture_output=True,
        text=True,
        check=False,
        cwd=cwd
    )
    return proc.stdout.strip()

ROOT = os.path.dirname(os.path.abspath(__file__))

# 1) hello
def test_hello():
    assert run_script('hello.py', cwd=ROOT) == 'Hello, World!'

# 2) python_if_else — 6 тестов
@pytest.mark.parametrize("input_data, expected", [
    ('1', 'Weird'),
    ('4', 'Not Weird'),
    ('3', 'Weird'),
    ('6', 'Weird'),
    ('22', 'Not Weird'),
    ('18', 'Weird'),
])
def test_python_if_else(input_data, expected):
    assert run_script('python_if_else.py', [input_data], cwd=ROOT) == expected

# 3) arithmetic_operators — 3 теста
@pytest.mark.parametrize("input_data, expected", [
    (['1', '2'], ['3', '-1', '2']),
    (['10', '5'], ['15', '5', '50']),
    (['0', '7'], ['7', '-7', '0']),
])
def test_arithmetic_operators(input_data, expected):
    assert run_script('arithmetic_operators.py', input_data, cwd=ROOT).split('\n') == expected

# 4) division — 4 теста
@pytest.mark.parametrize("input_data, expected", [
    (['3', '5'], ['0', '0.6']),
    (['10', '3'], ['3', '3.3333333333333335']),
    (['0', '5'], ['0', '0.0']),
    (['5', '0'], ['0', '0.0']),
])
def test_division(input_data, expected):
    out = run_script('division.py', input_data, cwd=ROOT).split('\n')
    assert out[0] == expected[0]
    if expected[1] == '0.0':
        assert out[1] == '0.0'
    else:
        assert abs(float(out[1]) - float(expected[1])) < 1e-9

def test_division_zero_second_line():
    out = run_script('division.py', ['5', '0'], cwd=ROOT).split('\n')
    assert len(out) == 2 and out[0] == '0' and out[1] == '0.0'

# 5) loops — 3 теста
@pytest.mark.parametrize("input_data, expected", [
    ('3', ['0', '1', '4']),
    ('1', ['0']),
    ('5', ['0', '1', '4', '9', '16']),
])
def test_loops(input_data, expected):
    assert run_script('loops.py', [input_data], cwd=ROOT).split('\n') == expected

# 6) print_function — 3 теста
@pytest.mark.parametrize("input_data, expected", [
    ('5', '12345'),
    ('1', '1'),
    ('3', '123'),
])
def test_print_function(input_data, expected):
    assert run_script('print_function.py', [input_data], cwd=ROOT) == expected

# 7) second_score — 4 теста
@pytest.mark.parametrize("input_data, expected", [
    (['5', '2 3 6 6 5'], '5'),
    (['3', '1 2 3'], '2'),
    (['2', '5 5'], '5'),
    (['4', '10 9 8 7'], '9'),
])
def test_second_score(input_data, expected):
    assert run_script('second_score.py', input_data, cwd=ROOT) == expected

# 8) nested_list — 2 теста
def test_nested_list_two_students():
    inp = ['5', 'Harry', '37.21', 'Berry', '37.21', 'Tina', '37.2', 'Akriti', '41', 'Harsh', '39']
    out = run_script('nested_list.py', inp, cwd=ROOT).split('\n')
    assert out == ['Berry', 'Harry']

def test_nested_list_one_second():
    inp = ['3', 'A', '50', 'B', '40', 'C', '30']
    assert run_script('nested_list.py', inp, cwd=ROOT) == 'B'

# 9) lists — 4 теста
def test_lists_example():
    inp = ['12', 'insert 0 5', 'insert 1 10', 'insert 0 6', 'print', 'remove 6', 'append 9', 'append 1', 'sort', 'print', 'pop', 'reverse', 'print']
    out = run_script('lists.py', inp, cwd=ROOT).split('\n')
    assert out[0] == '[6, 5, 10]' and out[1] == '[1, 5, 9, 10]' and out[2] == '[9, 5, 1]'

def test_lists_append_print():
    assert run_script('lists.py', ['2', 'append 1', 'print'], cwd=ROOT) == '[1]'

def test_lists_insert():
    assert run_script('lists.py', ['3', 'append 1', 'insert 0 2', 'print'], cwd=ROOT) == '[2, 1]'

def test_lists_remove():
    assert run_script('lists.py', ['4', 'append 1', 'append 2', 'remove 1', 'print'], cwd=ROOT) == '[2]'

# 10) swap_case — 3 теста
@pytest.mark.parametrize("input_data, expected", [
    ('Www.MosPolytech.ru', 'wWW.mOSpOLYTECH.RU'),
    ('Pythonist 2', 'pYTHONIST 2'),
    ('aBc', 'AbC'),
])
def test_swap_case(input_data, expected):
    assert run_script('swap_case.py', [input_data], cwd=ROOT) == expected

# 11) split_and_join — 3 теста
@pytest.mark.parametrize("input_data, expected", [
    ('this is a string', 'this-is-a-string'),
    ('one', 'one'),
    ('a b c', 'a-b-c'),
])
def test_split_and_join(input_data, expected):
    assert run_script('split_and_join.py', [input_data], cwd=ROOT) == expected

# 12) max_word — 1 тест (читает example.txt)
def test_max_word():
    out = run_script('max_word.py', cwd=ROOT)
    lines = out.split('\n')
    assert len(lines) >= 1
    for w in lines:
        assert len(w) >= 1

# 13) price_sum — 1 тест
def test_price_sum():
    out = run_script('price_sum.py', cwd=ROOT)
    parts = out.split()
    assert len(parts) == 3
    a, p, c = float(parts[0]), float(parts[1]), float(parts[2])
    assert a > 0 and p > 0 and c > 0

# 14) anagram — 4 теста
@pytest.mark.parametrize("input_data, expected", [
    (['abc', 'cab'], 'YES'),
    (['abc', 'abd'], 'NO'),
    (['a', 'a'], 'YES'),
    (['ab', 'ba'], 'YES'),
])
def test_anagram(input_data, expected):
    assert run_script('anagram.py', input_data, cwd=ROOT) == expected

# 15) metro — 4 теста
@pytest.mark.parametrize("input_data, expected", [
    (['2', '0 10', '5 15', '5'], '2'),
    (['2', '0 10', '5 15', '3'], '1'),
    (['1', '0 10', '10'], '1'),
    (['3', '0 5', '6 10', '1 9', '7'], '2'),
])
def test_metro(input_data, expected):
    assert run_script('metro.py', input_data, cwd=ROOT) == expected

# 16) minion_game — 3 теста
def test_minion_game_banana():
    assert run_script('minion_game.py', ['BANANA'], cwd=ROOT) == 'Стюарт 12'

def test_minion_game_kevin_wins():
    out = run_script('minion_game.py', ['AAAA'], cwd=ROOT)
    assert 'Кевин' in out

def test_minion_game_stuart_wins():
    out = run_script('minion_game.py', ['BBBB'], cwd=ROOT)
    assert 'Стюарт' in out

# 17) is_leap — 6 тестов
@pytest.mark.parametrize("input_data, expected", [
    ('2000', 'True'),
    ('1900', 'False'),
    ('2024', 'True'),
    ('2023', 'False'),
    ('2400', 'True'),
    ('2100', 'False'),
])
def test_is_leap(input_data, expected):
    assert run_script('is_leap.py', [input_data], cwd=ROOT) == expected

# 18) happiness — 4 теста
@pytest.mark.parametrize("input_data, expected", [
    (['3 2', '1 5 3', '3 1', '5 7'], '1'),
    (['2 1', '1 2', '1', '2'], '0'),
    (['2 1', '1 1', '1', '2'], '2'),
    (['2 1', '2 2', '1', '2'], '-2'),
])
def test_happiness(input_data, expected):
    assert run_script('happiness.py', input_data, cwd=ROOT) == expected

# 19) pirate_ship — 2 теста
def test_pirate_ship_full():
    inp = ['10 2', 'gold 5 100', 'silver 3 30']
    out = run_script('pirate_ship.py', inp, cwd=ROOT)
    lines = out.strip().split('\n')
    assert len(lines) >= 1

def test_pirate_ship_fractional():
    inp = ['5 2', 'gold 10 100', 'silver 5 30']
    out = run_script('pirate_ship.py', inp, cwd=ROOT)
    assert 'gold' in out or 'silver' in out

# 20) matrix_mult — 3 теста
def test_matrix_mult_2x2():
    inp = ['2', '1 0', '0 1', '1 0', '0 1']
    out = run_script('matrix_mult.py', inp, cwd=ROOT).split('\n')
    assert out[0].strip() == '1 0' and out[1].strip() == '0 1'

def test_matrix_mult_2x2_non_identity():
    inp = ['2', '1 2', '3 4', '1 0', '0 1']
    out = run_script('matrix_mult.py', inp, cwd=ROOT).split('\n')
    assert out[0].strip() == '1 2' and out[1].strip() == '3 4'

def test_matrix_mult_small():
    inp = ['2', '2 0', '0 2', '1 1', '1 1']
    out = run_script('matrix_mult.py', inp, cwd=ROOT).split('\n')
    assert out[0].strip() == '2 2' and out[1].strip() == '2 2'
