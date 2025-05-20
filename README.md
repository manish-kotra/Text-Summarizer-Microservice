# Text Summarizer Microservice

A Python-based microservice designed to generate concise summaries from large text inputs. Built with modular components, this project facilitates easy integration into larger applications and supports scalable deployment.

---

## Features

- **Modular Architecture**: Organized codebase with clear separation of concerns.
- **Summarization Pipeline**: Processes raw text through a series of components to produce summaries.
- **Configurable Parameters**: Easily adjust settings via YAML configuration files.
- **Logging**: Comprehensive logging for monitoring and debugging.
- **Docker Support**: Containerized setup for consistent deployment across environments.

---

## Project Structure

```
text-summarizer-microservice/
├── textSummarizer/
│   ├── components/
│   ├── config/
│   ├── constants/
│   ├── entity/
│   ├── logging/
│   ├── pipeline/
│   └── utils/
├── notebooks/
│   └── trial.ipynb
├── config/
│   └── config.yaml
├── parameters.yaml
├── app.py
├── main.py
├── requirements.txt
├── setup.py
├── Dockerfile
├── folder_template.py
└── README.md
```

---

## Installation

### Prerequisites

- Python 3.7 or higher
- pip package manager
- Docker (optional, for containerized deployment)

### Steps

1. **Clone the Repository**

```bash
git clone https://github.com/your-username/text-summarizer-microservice.git
cd text-summarizer-microservice
```

2. **Create a Virtual Environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install Dependencies**

```bash
pip install -r requirements.txt
```

4. **Configure Settings**

Edit `config/config.yaml` and `parameters.yaml` to adjust configurations as needed.

---

## Usage

### Running the Application

```bash
python main.py
```

This will initiate the summarization pipeline, processing input text and generating summaries based on the configured parameters.

### API Endpoint (Optional)

If `app.py` is set up with a web framework like Flask or FastAPI, you can run:

```bash
python app.py
```

This will start the web service, exposing endpoints for text summarization.

---

## Docker Deployment

1. **Build the Docker Image**

```bash
docker build -t text-summarizer-microservice .
```

2. **Run the Docker Container**

```bash
docker run -p 8000:8000 text-summarizer-microservice
```

This will start the service inside a Docker container, accessible at `http://localhost:8000`.

---

## Configuration Files

- **`config/config.yaml`**: Contains general configuration settings for the application.
- **`parameters.yaml`**: Holds parameters specific to the summarization process, such as model settings.

Ensure these files are properly configured before running the application.

---

## Utilities

- **`folder_template.py`**: Script to set up the project directory structure with necessary files and folders.
- **Logging**: Implemented using Python's `logging` module, with logs stored as per configurations in the `logging/` directory.

---
