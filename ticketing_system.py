from dataclasses import dataclass
from datetime import datetime
from typing import Dict, Optional

# =========================
# APPENDIX 1 – ZONES
# =========================

ZONES = {
    1: "Central",
    2: "Midtown",
    3: "Downtown"
}

# =========================
# APPENDIX 2 – FARES (CENTS PER ZONE)
# =========================

FARES_PER_ZONE = {
    "adult": 2105,
    "child": 1410,
    "senior": 1025,
    "student": 1750
}

CURRENCY = "cents"


# =========================
# DATA MODELS
# =========================

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


# =========================
# INPUT & VALIDATION
# =========================

def read_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def read_zone(prompt: str) -> int:
    while True:
        zone = read_int(prompt)
        if zone in ZONES:
            return zone
        print("Invalid zone. Please choose a valid zone number.")


def read_non_negative(prompt: str) -> int:
    while True:
        value = read_int(prompt)
        if value >= 0:
            return value
        print("Value cannot be negative.")


def read_travellers() -> Travellers:
    print("\nEnter number of travellers:")
    return Travellers(
        adult=read_non_negative("Adults: "),
        child=read_non_negative("Children: "),
        senior=read_non_negative("Seniors: "),
        student=read_non_negative("Students: ")
    )


# =========================
# CALCULATIONS
# =========================

def calculate_zones_travelled(start: int, end: int) -> int:
    return abs(end - start) + 1


def calculate_fares(travellers: Travellers, zones: int) -> Dict[str, int]:
    return {
        "Adult": travellers.adult * FARES_PER_ZONE["adult"] * zones,
        "Child": travellers.child * FARES_PER_ZONE["child"] * zones,
        "Senior": travellers.senior * FARES_PER_ZONE["senior"] * zones,
        "Student": travellers.student * FARES_PER_ZONE["student"] * zones
    }


# =========================
# VOUCHER OUTPUT
# =========================

def generate_voucher(ticket: Ticket) -> None:
    costs = calculate_fares(ticket.travellers, ticket.zones_travelled)
    total_cost = sum(costs.values())

    print("\n" + "=" * 50)
    print("CTA TRAVEL VOUCHER")
    print("=" * 50)
    print(f"Date/Time: {datetime.now()}")
    print(f"From Zone {ticket.start_zone} ({ZONES[ticket.start_zone]})")
    print(f"To Zone {ticket.end_zone} ({ZONES[ticket.end_zone]})")
    print(f"Zones Travelled: {ticket.zones_travelled}")
    print("-" * 50)

    for category, cost in costs.items():
        print(f"{category:<10}: {cost} {CURRENCY}")

    print("-" * 50)
    print(f"Total Travellers: {ticket.travellers.total()}")
    print(f"TOTAL COST: {total_cost} {CURRENCY}")
    print("=" * 50)


# =========================
# MAIN PROGRAM
# =========================

def main() -> None:
    print("CTA Underground Ticketing System")

    while True:
        print("\nZones:")
        for z, name in ZONES.items():
            print(f"{z}: {name}")

        start = read_zone("Enter starting zone: ")
        end = read_zone("Enter destination zone: ")

        travellers = read_travellers()
        if travellers.total() == 0:
            print("No travellers entered. Try again.")
            continue

        zones = calculate_zones_travelled(start, end)
        ticket = Ticket(start, end, zones, travellers)

        generate_voucher(ticket)

        again = input("\nIssue another voucher? (Y/N): ").lower()
        if again != "y":
            print("Program ended.")
            break


if __name__ == "__main__":
    main()
