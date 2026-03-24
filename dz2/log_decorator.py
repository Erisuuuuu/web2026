from datetime import datetime
from functools import wraps

def function_logger(filepath):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = datetime.now()
            try:
                result = func(*args, **kwargs)
            except Exception:
                raise
            end = datetime.now()
            with open(filepath, 'a', encoding='utf-8') as f:
                f.write(func.__name__ + '\n')
                f.write(start.strftime('%Y-%m-%d %H:%M:%S') + '.{:06d}\n'.format(start.microsecond))
                f.write(str(args) + '\n')
                if kwargs:
                    f.write(str(kwargs) + '\n')
                f.write((str(result) if result is not None else '-') + '\n')
                f.write(end.strftime('%Y-%m-%d %H:%M:%S') + '.{:06d}\n'.format(end.microsecond))
                delta = end - start
                f.write(str(delta) + '\n')
            return result
        return wrapper
    return decorator

if __name__ == '__main__':
    @function_logger('test.log')
    def greeting_format(name):
        return f'Hello, {name}!'
    greeting_format('John')
