import pandas as pd
from sklearn.model_selection import train_test_split

# Load data
dummy_file_path = '../data/test_data.csv'
dummy_data = pd.read_csv(dummy_file_path) 

# Choose target and features
y = dummy_data['Temperature (C)']
dummy_features = ['Formatted Date', 'Humidity', 'Wind Speed (km/h)',
       'Wind Bearing (degrees)', 'Visibility (km)', 'Loud Cover',
       'Pressure (millibars)']
X = dummy_data[dummy_features]


# split data into training and validation data, for both features and target
# The split is based on a random number generator. Supplying a numeric value to
# the random_state argument guarantees we get the same split every time we
# run this script.
train_X, val_X, train_y, val_y = train_test_split(X, y,random_state = 0)