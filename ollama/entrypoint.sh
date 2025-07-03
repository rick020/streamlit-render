#!/bin/sh

./bin/ollama serve &

sleep 5

curl -X POST http://localhost:11434/api/pull -d '{"name": "gemma:2b"}'

sleep 10

tail -f /dev/null