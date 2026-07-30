import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("millage", help="principale value needed", type=float)
    parser.add_argument("theta0", type=float, help="theta0", default=0.0, action="store_true")
    parser.add_argument("theta1", type=float, help="theta1", default=0.0, action="store_true")
    args = parser.parse_args()
    result = args.theta0 + args.theta1 * args.millage
    print(result)
    return


main()
