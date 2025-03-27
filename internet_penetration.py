import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Country":[
        "Russia", "China", "South Korea", "India", "Japan", 
        "Ethiopia", "Nigeria", "Egypt", "Mozambique", "South Africa", 
        "Mexico", "Brazil", "Argentina", "Costa Rica","Ecuador", "U.S.", 
        "Germany", "U.K.", "France", "Spain", 
        "Saudi Arabia", "United Arab", "Iraq", "Isreal" 
    ],
    
    "Region": [
        "Asia", "Asia", "Asia", "Asia", "Asia",
        "Africa", "Africa", "Africa", "Africa", "Africa",
        "Americas", "Americas", "Americas", "Americas", "Americas", "Americas",
        "Europe", "Europe", "Europe", "Europe",
        "Middle East", "Middle East", "Middle East", "Middle East"
    ],
    "Internet Penetration (%)": [
        92, 76, 97, 46, 85,
        22, 45, 72, 20, 72,
        72, 84, 88, 84, 72, 91,
        93, 97, 93, 95,
        100, 100, 78, 90
    ]
}

df = pd.DataFrame(data)

plt.figure(figsize=(12, 6))
bars = plt.barh(df["Country"], df["Internet Penetration (%)"], color="skyblue")

plt.xlabel("Internet Penetration (%)")
plt.ylabel("Country")
plt.title("Internet Penetration by Country")

plt.show()
