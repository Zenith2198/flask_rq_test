set -e
source .env

echo "Linting project..."
ruff check

if command -v python3 &>/dev/null; then
    PYTHON=python3
else
    PYTHON=python
fi
echo "Running predeploy..."
$PYTHON -m predeploy

echo "Starting hypercorn server..."
hypercorn --bind 0.0.0.0:$PORT --workers 8 main:app