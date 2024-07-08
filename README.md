# Data Analysis Agent

Welcome to the Data Analysis Agent! This tool allows you to upload your CSV data, ask questions about the data, and visualize the results. The app leverages the power of Large Language Models (LLMs) to provide insightful analysis and visualizations based on your queries.

## Features

- **CSV File Upload**: Easily upload your CSV data through the sidebar.
- **Data Analysis**: Enter queries about your data and get responses powered by LLMs.
- **Data Visualization**: Generate and display plots based on your data queries.

## How to Use

1. **Upload CSV**: Use the file uploader in the sidebar to upload your CSV file.
2. **Select Agent Type**: Choose the type of agent from the dropdown menu.
3. **Enter Query**: Input your query about the data in the text box.
4. **Run Query**: Click the "Run Query" button to get the analysis and visualizations.
5. **View Results**: See the generated plots and responses. The chat history is displayed below for reference.

## Demo

Check out the demo video below to see the app in action:

![Demo Video](./videos/demo_video_01.mp4)

## Installation

To run this app locally, follow these steps:

1. **Clone the repository**:

    ```bash
    git clone https://github.com/acn-thaihanguyen/DAGPT.git
    cd DAGPT
    ```

2. **Create a virtual environment**:

    ```bash
    python -m venv .venv
    source .venv/bin/activate   # On Windows use `.venv\Scripts\activate`
    ```

3. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:
    Create a `.env` file in the root directory of the project and add your environment variables. Example is provided in `.env.sample`:

    ```
    # API keys
    OPENAI_API_KEY=your_openai_api_key
    GOOGLE_API_KEY=your_google_api_key

    # Python path
    PYTHONPATH=/path/to/dagpt/folder
    ```

5. **Run the Streamlit app**:

    ```bash
    streamlit run app.py
    ```

Make sure to install all dependencies from the `requirements.txt` file.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
