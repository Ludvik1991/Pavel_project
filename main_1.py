import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

# cesta k souboru csv kde mám data.
soubor = r"D:\Python\Pavel_project\data\zaznam.csv"

# nacteni dat z csb souboru.
data = pd.read_csv(soubor)

# ukazka dat print
print(data.head())

# styl grafu- whitegrid
sns.set_style("whitegrid")


# normalni graf
plt.figure(figsize=(10, 6))

sns.lineplot(
    data=data,
    x="time",
    y="active_power_kw",
    marker="o"
)

plt.title("Vyroba fotovoltaicke elektrarny behem dne")
plt.xlabel("Cas")
plt.ylabel("Cinny vykon [kW]")

plt.tight_layout()
plt.savefig("graf_fve.png")
plt.show()


# zkouška animace
fig, ax = plt.subplots(figsize=(10, 6))

def update(i):
    ax.clear()

    sns.lineplot(
        data=data.iloc[:i+1],
        x="time",
        y="active_power_kw",
        marker="o",
        ax=ax
    )

    ax.set_title("Animace vyroby fotovoltaicke elektrarny")
    ax.set_xlabel("Cas")
    ax.set_ylabel("Cinny vykon [kW]")
    ax.set_ylim(0, data["active_power_kw"].max() + 5)

ani = FuncAnimation(
    fig,
    update,
    frames=len(data),
    repeat=False
)

ani.save("animace_fve.gif", writer=PillowWriter(fps=2))

print("Animace byla ulozena jako animace_fve.gif")