import argparse

def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file', type=str, help='First configuration file')
    parser.add_argument('second_file', type=str, help='Second configuration file')
    args = parser.parse_args()
    # Here you would call the function that does the comparison and show the difference
    # For now, we just print the received arguments
    print(f"Comparing {args.first_file} and {args.second_file}")

if __name__ == '__main__':
    main()
