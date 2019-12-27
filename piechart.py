import matplotlib.pyplot as plt
import subprocess

values = []
labels = []

sasia=int(input("Sa eshte numri i produkteve qe kerkon te paraqesesh? > "))

for i in range(sasia):
	labels.append(input("Fut emrin e produktit: "))

print(labels)

for i in range(sasia):
	values.append(int(input("Fut sasine e produktit(sipas rralles): ")))

plt.title("Perqindja e Produkteve te shitura")
plt.pie(values, labels=labels, autopct='%1.1f%%')

#plt.show
plt.savefig("prezantim.png")

#img = Image.open("prezantim.png")
#img.show()

subprocess.run("pwd")
subprocess.run("feh prezantim.png", shell=True)
