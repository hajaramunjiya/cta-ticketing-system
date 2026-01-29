# CTA Underground Ticketing System

## Overview
The CTA Underground Ticketing System is a Python-based console application that simulates an automated, zone-based ticketing solution for the Centrala Transport Authority (CTA). The system replaces manual ticket purchasing with a structured electronic process that improves accuracy, reduces waiting time, and enhances the passenger experience.

The application calculates fares based on the number of underground zones travelled and the category of each traveller, in accordance with the CTA client brief.

---

## Features
- Zone-based journey selection using CTA-defined zones
- Support for Adult, Child, Senior, and Student traveller categories
- Automatic calculation of zones travelled
- Fare calculation per traveller, per zone
- Strong input validation for zones and traveller quantities
- Prevention of invalid journeys (starting and destination zones must differ)
- Travel voucher generation including date and time of issue
- Multiple ticket transactions in a single session

---

## Zone-Based Fare Calculation
The underground network is divided into numbered zones.  
The number of zones travelled is calculated using the formula:

**Zones Travelled = |Destination Zone − Starting Zone| + 1**

This ensures that travel within the same or across multiple zones is charged accurately.

---

## Fare Structure
All fares are charged per traveller, per zone, in cents, as defined in Appendix 2:

| Category | Fare (cents per zone) |
|--------|------------------------|
| Adult  | 2105 |
| Child  | 1410 |
| Senior | 1025 |
| Student| 1750 |

---

## How the System Works
1. The user selects a starting zone from the available CTA zones.
2. The user selects a destination zone (must be different from the starting zone).
3. The user enters the number of travellers in each category.
4. The system validates all inputs.
5. The total fare is calculated based on zones travelled and traveller categories.
6. A formatted travel voucher is displayed.
7. The user may issue another voucher or exit the system.

---

## Sample Output
The generated travel voucher displays:
- Date and time of issue
- Boarding zone and destination zone
- Number of zones travelled
- Fare breakdown per traveller category
- Total number of travellers
- Final total cost

---

## Technologies Used
- Python 3
- Console-based user interface
- Procedural and object-oriented programming techniques
- Git version control for change tracking

---

## Running the Application
1. Ensure Python 3 is installed on the system.
2. Clone or download the project repository.
3. Navigate to the project directory.
4. Run the application using the command:python 
ticketing_system.py

The program will launch in the console and guide the user through the ticket purchasing process.
