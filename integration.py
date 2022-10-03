from numpy import sqrt

A = 1.2
B = 3


def expression(x: float) -> float:
    return (sqrt(2 * (x ** 2) + 0.7)) / (1.5 + sqrt(0.8 * x + 1))


def integrate_left_rect(step: float) -> float:
    x = A
    result = 0
    while x <= (B - step):
        result += expression(x)
        x += step
    return step * result


def integrate_right_rect(step: float) -> float:
    x = A + step
    result = 0
    while x <= B:
        result += expression(x)
        x += step
    return step * result


def integrate_trap(step: float) -> float:
    x = A + step
    result = 0
    while x <= (B - step):
        result += expression(x)
        x += step
    return ((expression(A) + expression(B)) / 2 + result) * step


def integrate_par(step: float) -> float:
    fraction_odd = 0
    x = A + step
    while x <= (B - step):
        fraction_odd += expression(x)
        x += 2 * step

    fraction_even = 0
    x = A + (2 * step)
    while x <= (B - (2 * step)):
        fraction_even += expression(x)
        x += 2 * step

    return (expression(A) + expression(B) + (4 * fraction_odd) + (2 * fraction_even)) * (step / 3)


def integrate_double_trap(eps: float) -> float:
    step = sqrt(eps)

    trap1 = 0
    trap2 = integrate_trap(step)
    if abs(trap1 - trap2) < eps:
        return trap2

    while abs(trap1 - trap2) >= eps:
        trap1 = trap2
        step /= 2
        trap2 = integrate_trap(step)
    return trap2
