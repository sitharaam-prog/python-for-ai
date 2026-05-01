import matplotlib.pyplot as plt

def draw_bar() :

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

def draw_pie() :

    # Data
    labels = ['Apples', 'Bananas', 'Cherries', 'Dates']
    sizes = [30, 25, 20, 25]

    # Create pie chart
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')

    # Add title
    plt.title('Fruit Distribution')

    # Show chart
    plt.show()