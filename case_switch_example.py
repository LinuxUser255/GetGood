def day_of_week(day: int) -> str:
    match day:
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"
        case 7:
            return "Sunday"
        case _:
            return "Invalid day"

def case_switch():
    print("Day of Week Example using match statement (Python 3.10+)")
    print("-" * 50)

    for i in range(1, 9):
        print(f"Day {i}: {day_of_week(i)}")

#if __name__ == "__main__":
#    main()