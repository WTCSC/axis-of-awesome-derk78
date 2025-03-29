import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Create a dataset with the countries, regions, and their internet penetration percentages using a dictionary.
data = {
    "Country":[
        "Russia", "China", "South Korea", "India", "Japan", 
        "Ethiopia", "Nigeria", "Egypt", "Mozambique", "South Africa", 
        "Mexico", "Brazil", "Argentina", "Costa Rica","Ecuador", "U.S.", 
        "Germany", "U.K.", "France", "Spain", 
        "Saudi Arabia", "Arab Emirates", "Iraq", "Isreal" 
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

#Define the output directory that the graph images will put into.
output_dir = "output"

#Create a pandas DataFrame using the dataset.
df = pd.DataFrame(data)

#Define the colors that we will be matching to each region.
region_colors = {
    "Asia": "lightblue",
    "Africa": "orange",
    "Americas": "green",
    "Europe": "purple",
    "Middle East": "red"
}


# Add a column that to the DataFrame that maps the different regions to their corresponding colors.
df["Color"] = df["Region"].map(region_colors)

# Create a horizontal bar chart to show the internet penetration for each of the countries that we found data on.
plt.figure(figsize=(16, 10)) # Define the figure size.
bars = plt.barh(df["Country"], df["Internet Penetration (%)"], color=df["Color"])

# Create the labels and title for the graph.
plt.ylabel("Internet Penetration (%)")
plt.xlabel("Country")
plt.title("Internet Penetration by Country")

#Create grid lines along the x axis to increase visiblity.
plt.grid(True, axis="x")

# Add the penetration percentages of each country.
plt.bar_label(bars, labels=[f"{percentage}%" for percentage in df["Internet Penetration (%)"]], color="black", fontweight="bold", padding=5)

#Import the pandas mpatch module to create a 2d shape that will go along with it's each regions color and name for the key.
handles = [
    mpatches.Patch(color=color, label=region)
    for region, color in region_colors.items()
]

#We use `.legend` to create the key that we just defined which will go in the upper right corner of the graph.
plt.legend(handles=handles, title="Region", loc="upper right")

# Save the bar chart as an image in the output directory while making sure to include the full path.
plt.savefig(f"{output_dir}/internet_penetration_by_country.png")


#Show the plot.
plt.show()

#Find the internet penetration of each region.
average_penetration = df.groupby("Region")["Internet Penetration (%)"].mean()

#Once we have the internet penetration of each region, find the average of all the regions internet penetration.
regions_average = df["Internet Penetration (%)"].mean()

plt.figure(figsize=(12, 6))#Set the figure size.

#plot the average internet penetration by region. 
# `Average_penetration.index` is the region names while `average_penetration.values` are the penetration values.
#`marker="o"` defines that each point of data will be marked with a circle and `linestyle="-"` defines that the line will be a dashed line.
plt.plot(average_penetration.index, average_penetration.values, marker="o", linestyle="-", color="green")

#Add a horizontal line for the overall average penetration rate of all the regions. Also create a label for the average line that legend will use to create a key at the bottom right of the graph.
plt.axhline(regions_average, color="orange", linestyle="--", label=f"Overall Average: {regions_average:.1f}%")

# Again create the labels and title for the graph.
plt.xlabel("Region")
plt.ylabel("Average Internet Penetration (%)")
plt.title("Average Internet Penetration per Region")
plt.ylim(0, 100)
plt.grid(True)

#Place the key using `.legend`
plt.legend(loc="lower right")

# Save the line graph as an image in the output directory.
plt.savefig(f"{output_dir}/average_internet_penetration_by_region.png")

plt.show()