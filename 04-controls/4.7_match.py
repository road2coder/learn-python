# match 在 3.10+ 才可以使用
def http_result(status_code: int):
    msg = 'ok'
    match status_code:
        case 400:
            msg = 'Bad request'
        case 404:
            msg = 'Not found'
        case 418:
            msg = "I'm a teapot "
        case 401 | 403:
            msg = 'Not allowed'
    print(msg)


http_result(400)


class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


point = Point(0, 10)

match point:
    case Point(x=0, y=0):
        print('point at Origin')
    case Point(x=0, y=y):
        print(f'point on the X axis at (0, {y})')
    case Point(x=x, y=0):
        print(f'point on the X axis at ({x}, 0)')
    case Point(x=x, y=y):
        print(f'point at ({x}, {y})')
