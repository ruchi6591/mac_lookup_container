
import sys
from macSearch import MacSearch

if __name__ == "__main__":
    try:
        if len(sys.argv) == 2:
            mac_address = str(sys.argv[1])
            lookup = MacSearch()
            lookup.mac_search(mac_address)
        else:
            print("Invalid parameters. Please check correct usage.")
    except Exception as ex:
        print("Invalid parameters. Please check correct usage.")
