import sys
import traceback

from clusterphuk.vm import VirtualMachine
from clusterphuk.vm_config import VMConfig

def main(argv):
    if len(argv) != 3:
        print(f'Usage: {argv[0]} <template> <config>')
        return 1

    template = VMConfig(argv[1])
    config = VMConfig(argv[2])

    config.merge_from(template)

    vm = VirtualMachine(config)
    vm.setup()

    try:
        vm.run()
    except Exception:
        traceback.print_exc()
        return 1
    finally:
        vm.teardown()

    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
