# DAGPT: Data Analysis GPT

DAGPT is a data analysis tool that uses GPT models to assist with data manipulation and analysis tasks via a conversational interface. This project leverages Streamlit to provide an interactive web application where users can upload their data, ask questions, and receive insights.

## Features

- **CSV File Upload**: Easily upload your CSV data through the sidebar.
- **Data Analysis**: Enter queries about your data and get responses powered by LLMs.
- **Data Visualization**: Generate and display plots based on your data queries.

## Application Interface

[Demo Image](images/demo_image_01.png)

## Getting Started

### Prerequisites

- Python 3.9 or higher
- pip (Python package installer)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/acn-thaihanguyen/DAGPT.git
   cd DAGPT
   ```

2. Create a virtual enviroment:

    ```
    python -m venv .venv
    source .venv/bin/activate   # On Windows use `.venv\Scripts\activate`
    ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
    Create a `.env` file in the root directory of the project and add your environment variables. Example is provided in `.env.sample`:

    ```
    # API keys
    OPENAI_API_KEY=your_openai_api_key
    GOOGLE_API_KEY=your_google_api_key

    # Python path
    PYTHONPATH=/path/to/dagpt/folder
    ```

### Running the Application

To start the Streamlit app, run the following command in your terminal:

```bash
streamlit run app.py
```

This will launch the web application in your default web browser.

### Usage

1. Upload a CSV file containing your data.
2. Use the text input to ask questions about the data.

## Project Structure

```
├── README.md
├── app.py
├── dagpt
│   ├── agents
│   │   ├── base.py
│   │   └── pandas_agent.py
│   ├── models
│   │   └── llms.py
│   ├── prompts
│   │   └── prompts.py
│   ├── tools
│   │   ├── tools.py
│   │   └── tools_ori.py
│   └── utils
│       └── utils.py
├── data
│   └── sample_data.csv
├── notebooks
├── requirements.txt
└── images
    └── demo_image_01.png
└── videos
    └── demo_video_01.mp4
```

### Project Components

- `app.py`: The main entry point for the Streamlit application.
- `dagpt/agents`: Contains the agent classes responsible for handling user queries.
  - `base.py`: Base class for agents.
  - `pandas_agent.py`: Agent specifically designed for handling pandas DataFrames.
- `dagpt/models`: Contains the language model classes.
  - `llms.py`: Class for interacting with GPT models.
- `dagpt/prompts`: Contains prompt templates for the agents.
  - `prompts.py`: Prompt templates for different scenarios.
- `dagpt/tools`: Contains utility tools for data manipulation and model interactions.
  - `tools.py`: Primary tools module.
  - `tools_ori.py`: Original tools module.
- `dagpt/utils`: General utility functions.
  - `utils.py`: Utility functions used throughout the project.
- `data`: Directory for storing sample data files.
  - `sample_data.csv`: A sample CSV file for testing.
- `notebooks`: Directory for Jupyter notebooks (for experiments and testing).
- `requirements.txt`: List of required Python packages.
- `images`: Directory for storing demo videos.
  - `demo_image_01.png`: A demo image showing the application interface.
- `videos`: Directory for storing demo videos.
  - `demo_video_01.mp4`: A demo video showing how to use the application.

### Demo Video

A demo video demonstrating how to use the application can be found in the `videos` folder: [demo_video_01.mp4](videos/demo_video_01.mp4)

## Contributing

Contributions are welcome! Please open an issue or submit a pull request on GitHub.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
