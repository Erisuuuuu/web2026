import os
import sys
import subprocess
import pytest

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT)

from fact import fact_rec, fact_it
from show_employee import show_employee
from sum_and_sub import sum_and_sub
from process_list import process_list, process_list_gen
from my_sum import my_sum
from email_validation import fun
from fibonacci import fibonacci
from average_scores import compute_average_scores
from plane_angle import plane_angle, Point
from phone_number import normalize
from people_sort import name_format
from circle_square_mk import circle_square_mk
from complex_numbers import Complex

def test_fact_rec_zero():
    assert fact_rec(0) == 1

def test_fact_rec_one():
    assert fact_rec(1) == 1

def test_fact_rec_five():
    assert fact_rec(5) == 120

def test_fact_rec_ten():
    assert fact_rec(10) == 3628800

def test_fact_it_zero():
    assert fact_it(0) == 1

def test_fact_it_one():
    assert fact_it(1) == 1

def test_fact_it_five():
    assert fact_it(5) == 120

def test_fact_it_ten():
    assert fact_it(10) == 3628800

def test_fact_rec_it_equal():
    for n in [0, 1, 2, 5, 10]:
        assert fact_rec(n) == fact_it(n)

def test_show_employee_default():
    assert show_employee('Иванов Иван Иванович') == 'Иванов Иван Иванович: 100000 ₽'

def test_show_employee_with_salary():
    assert show_employee('Петров', 30000) == 'Петров: 30000 ₽'

def test_show_employee_zero():
    assert show_employee('A', 0) == 'A: 0 ₽'

def test_sum_and_sub_positive():
    assert sum_and_sub(5, 3) == (8, 2)

def test_sum_and_sub_negative():
    assert sum_and_sub(-1, 4) == (3, -5)

def test_sum_and_sub_float():
    a, b = sum_and_sub(2.5, 1.5)
    assert abs(a - 4.0) < 1e-9 and abs(b - 1.0) < 1e-9

def test_sum_and_sub_zero():
    assert sum_and_sub(0, 0) == (0, 0)

def test_my_sum_empty():
    assert my_sum() == 0

def test_my_sum_one():
    assert my_sum(5) == 5

def test_my_sum_many():
    assert my_sum(1, 2, 3, 4, 5) == 15

def test_my_sum_float():
    assert abs(my_sum(0.1, 0.2) - 0.3) < 1e-9

def test_process_list_empty():
    assert process_list([]) == []

def test_process_list_one():
    assert process_list([1]) == [1]

def test_process_list_many():
    assert process_list([0, 1, 2]) == [0, 1, 4]

def test_process_list_gen_empty():
    assert list(process_list_gen([])) == []

def test_process_list_gen_many():
    assert list(process_list_gen([1, 2])) == [1, 4]

def test_fun_valid():
    assert fun('a@b.co') == True

def test_fun_valid_underscore():
    assert fun('user_name@site.com') == True

def test_fun_valid_dash():
    assert fun('user-name@site.ru') == True

def test_fun_invalid_no_at():
    assert fun('ab.co') == False

def test_fun_invalid_dot_extension():
    assert fun('a@b.coco') == False

def test_fun_invalid_empty():
    assert fun('') == False

def test_fun_invalid_extension_digit():
    assert fun('a@b.c1') == False

def test_fibonacci_zero():
    assert fibonacci(0) == []

def test_fibonacci_one():
    assert fibonacci(1) == [0]

def test_fibonacci_two():
    assert fibonacci(2) == [0, 1]

def test_fibonacci_five():
    assert fibonacci(5) == [0, 1, 1, 2, 3]

def test_fibonacci_ten():
    assert fibonacci(10)[:5] == [0, 1, 1, 2, 3]

def test_compute_average_scores_one_student():
    assert compute_average_scores([(100,), (80,)]) == (90.0,)

def test_compute_average_scores_two():
    assert compute_average_scores([(10, 20), (30, 40)]) == (20.0, 30.0)

def test_compute_average_scores_rounding():
    assert compute_average_scores([(89, 90, 78, 93, 80), (90, 91, 85, 88, 86), (91, 92, 83, 89, 90.5)]) == (90.0, 91.0, 82.0, 90.0, 85.5)

def test_plane_angle_right():
    A, B, C, D = Point(0, 0, 0), Point(1, 0, 0), Point(1, 1, 0), Point(0, 1, 1)
    angle = plane_angle(A, B, C, D)
    assert 0 <= angle <= 180

def test_plane_angle_same_plane():
    A, B, C, D = Point(0, 0, 0), Point(1, 0, 0), Point(1, 1, 0), Point(0, 1, 0)
    assert abs(plane_angle(A, B, C, D)) < 1e-6

def test_normalize_8():
    t = normalize('89875641230')
    assert t and t[1] == '+7 (987) 564-12-30'

def test_normalize_7():
    t = normalize('+79195969878')
    assert t and '919' in t[1]

def test_normalize_10():
    t = normalize('9195969878')
    assert t and t[0] == '9195969878'

def test_name_format_male():
    assert name_format([['Henry', 'Davids', '20', 'M']]) == ['Mr. Henry Davids']

def test_name_format_female():
    assert name_format([['Mary', 'George', '25', 'F']]) == ['Ms. Mary George']

def test_circle_square_mk_small():
    s = circle_square_mk(1, 10000)
    assert abs(s - 3.14159) < 0.5

def test_circle_square_mk_zero():
    assert circle_square_mk(1, 0) == 0

def test_complex_str_real():
    assert str(Complex(2.24, 0)) == '2.24+0.00i'

def test_complex_str_imag():
    s = str(Complex(0, 7.81))
    assert '0.00' in s and '7.81' in s

def test_complex_sum():
    c = Complex(2, 1) + Complex(5, 6)
    assert str(c) == '7.00+7.00i'

def run_script(name, args=None, stdin=None):
    if args is None:
        args = []
    cmd = [sys.executable, os.path.join(ROOT, name)] + args
    return subprocess.run(cmd, capture_output=True, text=True, input=stdin, cwd=ROOT, timeout=5)

def test_my_sum_argv():
    r = run_script('my_sum_argv.py', ['1', '2', '3', '4', '5'])
    assert r.returncode == 0 and r.stdout.strip() == '15'

def test_my_sum_argv_empty():
    r = run_script('my_sum_argv.py', [])
    assert r.returncode == 0 and r.stdout.strip() == '0'

def test_my_sum_argv_float():
    r = run_script('my_sum_argv.py', ['1.5', '2.5'])
    assert r.returncode == 0 and float(r.stdout.strip()) == 4.0

def test_files_sort_empty_dir(tmp_path):
    r = run_script('files_sort.py', [str(tmp_path)])
    assert r.returncode == 0 and r.stdout.strip() == ''

def test_files_sort_with_files(tmp_path):
    (tmp_path / 'a.py').write_text('')
    (tmp_path / 'b.txt').write_text('')
    (tmp_path / 'c.py').write_text('')
    r = run_script('files_sort.py', [str(tmp_path)])
    lines = r.stdout.strip().split('\n')
    assert lines == ['a.py', 'c.py', 'b.txt']

def test_file_search_not_found():
    r = run_script('file_search.py', ['nonexistent_file_xyz_12345.txt'])
    assert r.returncode == 0 and 'не найден' in r.stdout

def test_email_validation_main():
    r = run_script('email_validation.py', [], stdin='3\nlara@mospolytech.ru\nbrian-23@mospolytech.ru\nbritts_54@mospolytech.ru\n')
    assert r.returncode == 0
    out = r.stdout.strip()
    assert 'lara' in out and 'brian' in out and 'britts' in out

def test_fibonacci_main():
    r = run_script('fibonacci.py', [], stdin='5\n')
    assert r.returncode == 0 and '[0, 1, 1, 8, 27]' in r.stdout

def test_people_sort_main():
    r = run_script('people_sort.py', [], stdin='3\nMike Thomson 20 M\nRobert Bustle 32 M\nAndria Bustle 30 F\n')
    assert r.returncode == 0
    lines = r.stdout.strip().split('\n')
    assert 'Mike' in lines[0] and 'Andria' in lines[1] and 'Robert' in lines[2]

def test_phone_number_main():
    r = run_script('phone_number.py', [], stdin='3\n07895462130\n89875641230\n9195969878\n')
    assert r.returncode == 0
    out = r.stdout
    assert '+7 (789)' in out and '+7 (919)' in out and '+7 (987)' in out

def test_complex_numbers_main():
    r = run_script('complex_numbers.py', [], stdin='2 1\n5 6\n')
    assert r.returncode == 0
    lines = r.stdout.strip().split('\n')
    assert len(lines) >= 6 and '7.00+7.00i' in lines[0]

def test_average_scores_main():
    r = run_script('average_scores.py', [], stdin='5 3\n89 90 78 93 80\n90 91 85 88 86\n91 92 83 89 90.5\n')
    assert r.returncode == 0
    lines = [l.strip() for l in r.stdout.strip().split('\n')]
    assert '90.0' in lines and '85.5' in lines

def test_log_decorator():
    from log_decorator import function_logger
    import tempfile
    with tempfile.NamedTemporaryFile(mode='w', suffix='.log', delete=False) as tf:
        logpath = tf.name
    try:
        @function_logger(logpath)
        def add(a, b):
            return a + b
        add(1, 2)
        with open(logpath, 'r') as f:
            content = f.read()
        assert 'add' in content and '3' in content
    finally:
        try:
            os.unlink(logpath)
        except Exception:
            pass
