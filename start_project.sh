#!/bin/bash

# Define the Ollama server port
OLLAMA_PORT=11434

# Function to check if Ollama is running
is_ollama_running() {
    lsof -i :$OLLAMA_PORT | grep LISTEN > /dev/null
    return $?
}

echo "🔄 Checking if Ollama is running..."

if is_ollama_running; then
    echo "✅ Ollama is already running on port $OLLAMA_PORT."
else
    echo "🚀 Starting Ollama server..."
    nohup ollama serve > ollama.log 2>&1 &
    sleep 3  # Give it time to initialize
    echo "✅ Ollama started in the background."
fi

echo "🛠️ Launching Streamlit frontend..."


streamlit run frontend/app.py
