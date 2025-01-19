# Combined Cycle Power Plant Prediction Using Artificial Neural Networks

This project utilizes an Artificial Neural Network (ANN) to predict target variables based on features from a dataset related to a combined cycle power plant. The model is implemented using TensorFlow and Keras and trained on structured data provided in an Excel file.

## Dataset

The dataset is included as an Excel file with 5 sheets:
- **Sheet1**, **Sheet2**, **Sheet3**, **Sheet4**, **Sheet5**: Each contains 5 columns (features and target) and multiple rows of data.

The features (`X`) are extracted from all columns except the last, which serves as the target (`y`).

## Features

1. **Libraries Used**:
   - Python 3.x
   - NumPy
   - Pandas
   - TensorFlow (Keras)
   - Scikit-learn

2. **Workflow**:
   - **Data Preprocessing**: Load the dataset and split it into features (`X`) and target (`y`).
   - **Data Splitting**: Use `train_test_split` to divide the data into training and testing sets.
   - **Model Creation**: Build a sequential ANN with two hidden layers using ReLU activation functions.
   - **Model Compilation**: Use Adam optimizer and mean squared error as the loss function.
   - **Model Training**: Train the ANN for 100 epochs with a batch size of 32.
   - **Prediction**: Evaluate the model on the test set and compare predictions with actual values.

## Usage

### Prerequisites
- Python 3.7+
- TensorFlow 2.x
- Pandas
- NumPy
- Scikit-learn

### Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Project
1. Place the dataset file (`dataset.xlsx`) in the root directory.
2. Run the Jupyter Notebook:
   ```bash
   jupyter notebook Combined_Cycle_Power_Plant_using_Artificial_Neural_Network.ipynb
   ```
3. Follow the cells in the notebook to execute the workflow.



## Results
The trained ANN provides predictions for the target variable with reasonable accuracy, suitable for regression tasks in power plant datasets.

## Contributing
Contributions are welcome! Please create an issue or submit a pull request for any suggestions or improvements.

## License
This project is licensed under the MIT License. See `LICENSE` for more details.

