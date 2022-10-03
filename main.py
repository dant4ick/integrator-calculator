from integration import *

if __name__ == '__main__':
    for i in [10, 100, 1000, 10000]:
        print(f"split is {i}")
        print(f"{integrate_left_rect((B - A) / i) = }")
        print(f"{integrate_right_rect((B - A) / i) = }")
        print(f"{integrate_trap((B - A) / i) = }")
        print(f"{integrate_par((B - A) / i) = }")
        print('\n')

    print(integrate_double_trap(.00000001))
