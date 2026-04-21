set -e

echo "Formatting project..."
ruff format

if command -v python3 &>/dev/null; then
    PYTHON=python3
else
    PYTHON=python
fi

echo "Starting server in dev mode..."
$PYTHON -m main