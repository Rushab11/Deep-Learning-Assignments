import matplotlib.pyplot as plt

data = {
    "Help and Documentation": 3.40,
    "Help users recover from errors": 4.15,
    "Aesthetic and minimalistic design": 4.30,
    "Flexibility and efficiency of use": 3.80,
    "Recognition rather than recall": 4.00,
    "Error prevention": 4.15,
    "Consistency and Standards": 4.70,
    "User control and freedom": 3.95,
    "Match between system and the real world": 4,
    "Visibility of system status": 4.35,
}

labels = list(data.keys())
ratings = list(data.values())

fig = plt.figure(figsize=(10, 8))  # Set the desired width and height of the figure

plt.barh(range(len(labels)), ratings, align='center', fill=False, hatch="xxx")
plt.yticks(range(len(labels)), labels, fontsize=12)
plt.xlabel('Rating')
plt.title('User Experience Ratings')

for i, v in enumerate(ratings):
    plt.text(v+0.05, i, str(v), color='black', va="center", fontweight="bold",
             bbox=dict(facecolor='none', edgecolor='none', boxstyle='round', alpha=0.0))

plt.savefig('plot.png', dpi=300, bbox_inches='tight')
