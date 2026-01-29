from dataclasses import dataclass
from datetime import datetime
from typing import Dict


ZONES = {
    1: "Central",
    2: "Midtown",
    3: "Downtown"
}

FARES_PER_ZONE = {
    "adult": 2105,
    "child": 1410,
    "senior": 1025,
    "student": 1750
}

CURRENCY = "cents"


@dataclass
class Travellers:
    adult: int = 0
    child: int = 0
    senior: int = 0
    student: int = 0

    def total(self) -> int:
        return self.adult + self.child + self.senior + self.student


@dataclass
class Ticket:
    start_zone: int
    end_zone: int
    zones_travelled: int
    travellers: Travellers


def read_int(prompt: str) -> int:
    while True:
        raw = input(prompt).strip()
        try:
            return int(raw)
        except ValueError:
            print("Error: Please enter a valid whole number.")


def read_zone(prompt: str) -> int:
    while True:
        zone = read_int(prompt)
        if zone in ZONES:
            return zone
        print(f"Error: Invalid zone. Choose a zone between {min(ZONES)} and {max(ZONES)}.")


def read_non_negative(prompt: str) -> int:
    while True:
        value = read_int(prompt)
        if value >= 0:
            return value
        print("Error: Value cannot be negative.")


def read_travellers() -> Travellers:
    print("\nEnter number of travellers:")
    return Travellers(
        adult=read_non_negative("Adults: "),
        child=read_non_negative("Children: "),
        senior=read_non_negative("Seniors: "),
        student=read_non_negative("Students: ")
    )


def calculate_zones_travelled(start: int, end: int) -> int:
    return abs(end - start) + 1


def calculate_fares(travellers: Travellers, zones: int) -> Dict[str, int]:
    return {
        "Adult": travellers.adult * FARES_PER_ZONE["adult"] * zones,
        "Child": travellers.child * FARES_PER_ZONE["child"] * zones,
        "Senior": travellers.senior * FARES_PER_ZONE["senior"] * zones,
        "Student": travellers.student * FARES_PER_ZONE["student"] * zones
    }


def generate_voucher(ticket: Ticket) -> None:
    costs = calculate_fares(ticket.travellers, ticket.zones_travelled)
    total_cost = sum(costs.values())

    print("\n" + "=" * 50)
    print("CTA TRAVEL VOUCHER")
    print("=" * 50)
    print(f"Date/Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"From Zone {ticket.start_zone} ({ZONES[ticket.start_zone]})")
    print(f"To   Zone {ticket.end_zone} ({ZONES[ticket.end_zone]})")
    print(f"Zones Travelled: {ticket.zones_travelled}")
    print("-" * 50)

    for category, cost in costs.items():
        print(f"{category:<10}: {cost} {CURRENCY}")

    print("-" * 50)
    print(f"Total Travellers: {ticket.travellers.total()}")
    print(f"TOTAL COST: {total_cost} {CURRENCY}")
    print("=" * 50)


def main() -> None:
    print("CTA Underground Ticketing System")

    while True:
        print("\nZones:")
        for z, name in ZONES.items():
            print(f"{z}: {name}")

        start = read_zone("Enter starting zone: ")

        # Destination must be different to avoid invalid/pointless journey
        while True:
            end = read_zone("Enter destination zone: ")
            if end != start:
                break
            print("Error: Destination zone cannot be the same as starting zone. Please re-enter.")

        travellers = read_travellers()
        if travellers.total() == 0:
            print("Error: No travellers entered. Try again.")
            continue

        zones = calculate_zones_travelled(start, end)
        ticket = Ticket(start, end, zones, travellers)
        generate_voucher(ticket)

        again = input("\nIssue another voucher? (Y/N): ").strip().lower()
        if again != "y":
            print("Program ended.")
            break


if __name__ == "__main__":
    main()
