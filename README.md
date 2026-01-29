# CTA Underground Ticketing System

## Overview
The CTA Underground Ticketing System is a Python-based console application that simulates an automated, zone-based ticketing solution for an underground transport network. The system replaces manual ticket purchasing with a structured electronic process that calculates fares based on the number of zones travelled and traveller categories.

---

## Features
- Zone-based journey selection
- Support for Adult, Child, Senior, and Student travellers
- Automatic calculation of zones travelled
- Fare calculation per zone
- Input validation for zones and traveller quantities
- Travel voucher generation with date and time
- Multiple ticket transactions in a single session

---

## Zone-Based Fare Calculation
The underground network is divided into zones. The number of zones travelled is calculated using:

Zones Travelled = |Destination Zone − Starting Zone| + 1

Fares are calculated based on the traveller category and the number of zones travelled.

---

## Fare Structure
All fares are charged per traveller, per zone, in cents:

| Category | Fare (cents per zone) |
|---------|------------------------|
| Adult   | 2105                   |
| Child   | 1410                   |
| Senior  | 1025                   |
| Student | 1750                   |

---

## How the System Works
1. Select a starting zone
2. Select a destination zone
3. Enter the number of travellers for each category
4. The system calculates the total fare
5. A travel voucher is displayed
6. Choose to issue another voucher or exit

---

## Sample Output
The travel voucher displays:
- Date and time of issue
- Boarding and destination zones
- Number of zones travelled
- Fare breakdown per traveller category
- Total number of travellers
- Final total cost

---

## Technologies Used
- Python 3
- Console-based interface
- Procedural and object-oriented programming
- Git version control

---

## Running the Application
1. Ensure Python 3 is installed.
2. Clone or download the repository.
3. Run the application using:

