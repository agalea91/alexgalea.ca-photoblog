#!/bin/bash
echo "cd eb-app"
cd eb-app
echo "export FLASK_ENV=development"
export FLASK_ENV=development
echo ".venv/bin/python application.py"
.venv/bin/python application.py
