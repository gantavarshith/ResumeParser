# Resume Scraper

An automated tool to extract structured data from resumes (PDF/DOCX) using LLMs (OpenAI or Google Gemini).


    Create a `.env` file in the root directory and add your API keys:
    ```env
    OPENAI_API_KEY=your_openai_key
    GOOGLE_API_KEY=your_gemini_key
    ```


I had difficulty with venv so I've included startup scripts that automatically handle the virtual environment activation:

Double-click `run.bat` or run:
```cmd
run.bat
```

Run:
```powershell
./run.ps1
```

The script will:
1. Create the virtual environment if it doesn't exist.
2. Activate it.
3. Install/Update dependencies.
4. Start the FastAPI server on `http://127.0.0.1:8000`.

Once the server is running, visit `http://127.0.0.1:8000/docs` to test the API.
