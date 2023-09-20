def convert_ab_to_int(a: str, b: str) -> tuple[int,int]:
    a, b = int(a), int(b)
    return a, b

def divide_ab(a: int | float, b: int | float) -> float:
    raise IndentationError
    if 3 in [a, b]:
        raise Exception('Я ненавижу тройки')
    return a / b

while True:
    a, b = input('Введите два числа для их суммы:').split()
    try:
        a, b = convert_ab_to_int(a, b)
        division_score = divide_ab(a,b)
    except Exception:
        print('люблю ошибки')
    except (ZeroDivisionError, ValueError) as e:
        print(f'Ошибка: {e}')
        print('Введи числа и без нулей!')
        print()
        continue
    except AttributeError as ex:
        print(f'Разработчик злой')
        print('сделай пж как он просит')
        break
    finally:
        print('мы в финале шоу танцы')

    ab_sum = a + b
    print(f'Сумма {a} + {b} = {ab_sum}')
    print(f'{a} / {b} = {division_score}')
    print()