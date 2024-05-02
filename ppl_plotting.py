import pandas as pd
import matplotlib.pyplot as plt

# Load the data from a CSV file
df = pd.read_csv('output.csv')


# Create a "validation ppl" column that increases by 500 for each row
df["validation ppl"] = [500 * (i + 1) for i in range(len(df))]




# Plot the data using the correct column names for the logs
df.plot(x="validation ppl", y=["baseline.log", "prenorm.log", "postnorm.log"])  # Assuming the correct column names are these

# add a title to the plot
plt.title('ppl values for different models at each validation step')

# save plot to png file
plt.savefig('ppl_plot.png')
