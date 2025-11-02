months = {
    "January": "01",
    "February": "02",
    "March": "03",
    "April": "04",
    "May": "05",
    "June": "06",
    "July": "07",
    "August": "08",
    "September": "09",
    "October": "10",
    "November": "11",
    "December": "12"
}

while True:
    date = input("Date: ").strip()
    
    if "/" in date:
        try:
            month, day, year = date.split("/")
            month = month.zfill(2)
            day = day.zfill(2)
            year = year.zfill(4)
                
            if 1 <= int(month) <= 12 and 1 <= int(day) <= 31:
                print(f"{year}-{month}-{day}")
                break
        
        except ValueError:
            continue

    else:
        try:
            parts = date.split()
            if len(parts) != 3:
                continue
            
            month_name = parts[0]
            day = parts[1].rstrip(",")
            year = parts[2]
            
            if month_name not in months:
                continue
            if not parts[1].endswith(","):
                continue 
            
            month = months[month_name]
            day = day.zfill(2)
            
            if len(year) == 4 and year.isdigit() and 1 <= int(day) <= 31:
                print(f"{year}-{month}-{day}")
                break
            
        except (ValueError, IndexError):
            continue
    