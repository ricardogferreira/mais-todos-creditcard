#!/bin/sh

uvicorn src.main:app --host 0.0.0.0 --port 5000 --reload --log-level info --workers 1
