# PDF Parser API

A simple API to parse PDF files using a Gemini key. This project includes a `/docs` route for interactive API documentation via Swagger UI.

## 🚀 Getting Started

Follow the steps below to set up and run the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/pdf-parser-api.git
cd pdf-parser-api
```

### 2. Create and Activate Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (macOS/Linux)
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Gemini API Key

Create a `.env` file in the root directory and add your Gemini API key:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

### 5. Run the Application

```bash
python main.py
```

### 6. Access the API Documentation

Open your browser and navigate to:

```
http://localhost:8000/docs
```

From there, you can test the `/pdf_parser` endpoint and other available routes.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
