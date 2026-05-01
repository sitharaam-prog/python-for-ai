import matplotlib.pyplot as plt

# Data
labels = ['Apples', 'Bananas', 'Cherries', 'Dates']
sizes = [30, 25, 20, 25]

# Create pie chart
plt.pie(sizes, labels=labels, autopct='%1.1f%%')

# Add title
plt.title('Fruit Distribution')

# Show chart
plt.show()