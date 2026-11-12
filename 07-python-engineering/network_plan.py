"""Validate CIDR network ranges and report overlaps."""
from __future__ import annotations

import argparse
import ipaddress
import sys
from collections.abc import Sequence


def find_overlaps(cidr_ranges: Sequence[str]) -> list[tuple[str, str]]:
    """Return every pair of overlapping IPv4/IPv6 networks."""
    networks = [(value, ipaddress.ip_network(value, strict=True)) for value in cidr_ranges]
    overlaps: list[tuple[str, str]] = []

    for index, (left_text, left_network) in enumerate(networks):
        for right_text, right_network in networks[index + 1 :]:
            if left_network.version == right_network.version and left_network.overlaps(right_network):
                overlaps.append((left_text, right_text))
    return overlaps


def main() -> int:
    parser = argparse.ArgumentParser(description="Check CIDR ranges for overlap.")
    parser.add_argument("cidrs", nargs="+", help="IPv4 or IPv6 CIDR ranges.")
    parser.add_argument("--strict", action="store_true",
                        help="Return non-zero when overlapping networks are found.")
    args = parser.parse_args()

    try:
        overlaps = find_overlaps(args.cidrs)
    except ValueError as exc:
        print(f"Invalid network: {exc}", file=sys.stderr)
        return 2

    if not overlaps:
        print("OK: no overlapping CIDR ranges found.")
        return 0
    print("Overlapping CIDR ranges:")
    for left, right in overlaps:
        print(f" - {left} overlaps {right}")
    return 1 if args.strict else 0


if __name__ == "__main__":
    raise SystemExit(main())
