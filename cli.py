import argparse
from recursive_evolution_demo.run_demo import main

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Recursive Paradox Governance CLI")
    parser.add_argument("--run-demo", action="store_true")
    args = parser.parse_args()

    if args.run_demo:
        main()
