import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

people = [
    ("Afeerah", 20),
    ("Aliba", 25),
    ("Rabia", 30),
    ("Mubeen", 40),
    ("Hadia", 35),
]

ages = [a for n, a in people]
names = [n for n, a in people]

print("Total age:", sum(ages))
print("Average age:", sum(ages) / len(ages))
print("Highest age:", max(ages))
print("Lowest age:", min(ages))

plt.bar(names, ages)
plt.title("Age Comparison Graph")
plt.xlabel("Name")
plt.ylabel("Age")
plt.savefig("age_graph.png")
