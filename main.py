from utils import clear, header
from console import CashMachineConsole


def main():
    clear()

    header()

    CashMachineConsole.call_operation()


if __name__ == '__main__':
    while True:
        main()

        input('Pressione <ENTER> para continuar...')