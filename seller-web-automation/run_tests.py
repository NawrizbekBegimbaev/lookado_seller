#!/usr/bin/env python3
"""
Helper script to run pytest with timestamped HTML reports.

Usage Examples:
    # Run all tests
    python run_tests.py

    # Run smoke tests only
    python run_tests.py --smoke

    # Run specific test file
    python run_tests.py --file tests/test_login.py

    # Run with custom browser
    python run_tests.py --browser firefox

    # Run with custom URL
    python run_tests.py --url https://staging-seller.aralash.uz
"""

import sys
import subprocess
from datetime import datetime
from pathlib import Path
import argparse


def generate_report_filename(test_type="all"):
    """Generate timestamped report filename."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"reports/{test_type}_{timestamp}.html"


def run_tests(args):
    """Run pytest with specified arguments."""
    # Create reports directory if it doesn't exist
    reports_dir = Path("reports")
    reports_dir.mkdir(exist_ok=True)

    # Base pytest command
    pytest_cmd = ["pytest", "-v"]

    # Add test selection
    if args.smoke:
        pytest_cmd.extend(["-m", "smoke"])
        report_file = generate_report_filename("smoke")
    elif args.file:
        pytest_cmd.append(args.file)
        # Extract test name from file path for report naming
        test_name = Path(args.file).stem
        report_file = generate_report_filename(test_name)
    elif args.marker:
        pytest_cmd.extend(["-m", args.marker])
        report_file = generate_report_filename(args.marker)
    else:
        report_file = generate_report_filename("all")

    # Add HTML report
    pytest_cmd.extend([
        f"--html={report_file}",
        "--self-contained-html"
    ])

    # Add browser option
    if args.browser:
        pytest_cmd.append(f"--browser_name={args.browser}")

    # Add URL option
    if args.url:
        pytest_cmd.append(f"--url_name={args.url}")

    # Add verbosity
    if args.verbose:
        pytest_cmd.append("-vv")

    # Add maxfail option
    if args.maxfail:
        pytest_cmd.append(f"--maxfail={args.maxfail}")

    # Print command
    print("=" * 80)
    print(f"Running: {' '.join(pytest_cmd)}")
    print(f"Report will be saved to: {report_file}")
    print("=" * 80)

    # Run pytest
    result = subprocess.run(pytest_cmd)

    # Print report location
    print("\n" + "=" * 80)
    if result.returncode == 0:
        print(f"✓ Tests passed! Report: {report_file}")
    else:
        print(f"✗ Tests failed! Check report: {report_file}")
    print("=" * 80)

    return result.returncode


def main():
    parser = argparse.ArgumentParser(
        description="Run pytest with timestamped HTML reports",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python run_tests.py                           # Run all tests
  python run_tests.py --smoke                   # Run smoke tests
  python run_tests.py --file tests/test_login.py  # Run specific file
  python run_tests.py --marker functional       # Run tests with marker
  python run_tests.py --browser firefox         # Use Firefox
  python run_tests.py --url https://staging-seller.aralash.uz  # Custom URL
        """
    )

    parser.add_argument(
        "--smoke",
        action="store_true",
        help="Run only smoke tests"
    )
    parser.add_argument(
        "--file",
        type=str,
        help="Run specific test file"
    )
    parser.add_argument(
        "--marker",
        type=str,
        help="Run tests with specific marker (smoke, negative, functional)"
    )
    parser.add_argument(
        "--browser",
        type=str,
        choices=["chrome", "chromium", "firefox", "webkit"],
        default="chrome",
        help="Browser to use for tests (default: chrome)"
    )
    parser.add_argument(
        "--url",
        type=str,
        help="Base URL for tests"
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Extra verbose output"
    )
    parser.add_argument(
        "--maxfail",
        type=int,
        help="Stop after N failures"
    )

    args = parser.parse_args()

    # Run tests
    sys.exit(run_tests(args))


if __name__ == "__main__":
    main()