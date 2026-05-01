import matplotlib.pyplot as plt

# Data
labels = ['Apples', 'Bananas', 'Cherries', 'Dates']
sizes = [30, 25, 20, 25]

# Create bar chart
plt.bar(labels, sizes)

# Add title and labels
plt.title('Fruit Distribution')
plt.xlabel('Fruits')
plt.ylabel('Quantity')

# Show chart
plt.show()