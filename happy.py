import matplotlib.pyplot as plt

def input_happiness_scores():
    # Define the criteria
    criteria = [
        "Health",
        "Relationships",
        "Work-life Balance",
        "Financial Stability",
        "Personal Growth",
        "Leisure Activities"
    ]
    
    # Collect scores
    scores = []
    print("Rate your happiness for each criterion on a scale of 1 to 10:")
    for criterion in criteria:
        while True:
            try:
                score = int(input(f"{criterion}: "))
                if 1 <= score <= 10:
                    scores.append(score)
                    break
                else:
                    print("Please enter a number between 1 and 10.")
            except ValueError:
                print("Invalid input. Please enter an integer.")
    return criteria, scores

def create_pie_chart(criteria, scores):
    # Plot pie chart
    plt.figure(figsize=(8, 8))
    plt.pie(scores, labels=criteria, autopct='%1.1f%%', startangle=140)
    plt.title("Happiness Distribution")
    plt.show()

# Main Program
if __name__ == "__main__":
    criteria, scores = input_happiness_scores()
    create_pie_chart(criteria, scores)
