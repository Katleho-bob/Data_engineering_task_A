from datetime import datetime

def parse_datetime(dt_str):
    return datetime.strptime(dt_str, "%a %d %b %Y %H:%M:%S %z")

def calculate_difference(t1, t2):
    dt1 = parse_datetime(t1)
    dt2 = parse_datetime(t2)
    return str(abs(int((dt1 - dt2).total_seconds())))

def main():
    print("    Please paste your sample input below.")
    print("    First, enter the number of test cases, followed by each pair of timestamps:")
    print("    (Example format: 2, then 4 lines of timestamps)\n")

    T = int(input("Number of test cases: "))
    results = []
    for i in range(T):
        t1 = input(f"\nEnter timestamp t1 for test case #{i + 1}: ").strip()
        t2 = input(f"Enter timestamp t2 for test case #{i + 1}: ").strip()
        results.append(calculate_difference(t1, t2))

    print("\n Output:")
    for r in results:
        print(r)

if __name__ == "__main__":
    main()
