if (-not (Test-Path venv)) {
    Write-Host "Creating virtual environment..." -ForegroundColor Cyan
    python -m venv venv
}

Write-Host "Activating virtual environment..." -ForegroundColor Cyan
. venv\Scripts\Activate.ps1

Write-Host "Installing dependencies..." -ForegroundColor Cyan
pip install -r requirements.txt

Write-Host "Starting Resume Scraper..." -ForegroundColor Cyan
uvicorn app.main:app --reload
