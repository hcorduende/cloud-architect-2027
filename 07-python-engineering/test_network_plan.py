import unittest

from network_plan import find_overlaps


class FindOverlapsTests(unittest.TestCase):
    def test_detects_subnet_inside_vnet(self) -> None:
        self.assertEqual(
            find_overlaps(["10.20.0.0/16", "10.20.1.0/24"]),
            [("10.20.0.0/16", "10.20.1.0/24")],
        )

    def test_allows_non_overlapping_networks(self) -> None:
        self.assertEqual(
            find_overlaps(["10.20.1.0/24", "10.20.2.0/24", "2001:db8::/32"]),
            [],
        )

    def test_detects_nested_overlaps(self) -> None:
        self.assertEqual(
            find_overlaps(["10.20.1.0/24", "10.20.1.128/25"]),
            [("10.20.1.0/24", "10.20.1.128/25")],
        )

    def test_rejects_host_bits_in_strict_cidr(self) -> None:
        with self.assertRaises(ValueError):
            find_overlaps(["10.20.1.1/24"])


if __name__ == "__main__":
    unittest.main()
