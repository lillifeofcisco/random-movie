# CISCOS

This is a Streamlit-based Movie Recommender System.

## Setup

1.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

2.  **Generate Mock Data**:
    Since the original data files are not included, you must generate mock data to run the application:
    ```bash
    python3 generate_mock_data.py
    ```

3.  **Run the Application**:
    ```bash
    streamlit run app.py
    ```

## Files

- `app.py`: The main Streamlit application.
- `generate_mock_data.py`: Script to generate dummy data files for demonstration.
- `requirements.txt`: List of Python dependencies.
- `movie_dict.pkl`, `collab_titles.pkl`, `similarity.pkl.gz`, `collab_similarity.pkl.gz`: Generated mock data files required for the app to run. These are included in the repository but can be regenerated using `generate_mock_data.py`.

## Configuration (Optional)

To enable the "Forgot Password" functionality via email, you need to configure your email credentials.

1.  Create a `.streamlit` folder in the project root.
2.  Create a `secrets.toml` file inside `.streamlit/`.
3.  Add your email credentials:

    ```toml
    SENDER_EMAIL = "your-email@gmail.com"
    APP_PASSWORD = "your-app-password"
    ```

*Note: For Gmail, you will need to generate an App Password.*
