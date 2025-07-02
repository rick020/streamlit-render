FROM ollama/ollama

# Optional: pull a model before serving
# RUN ollama serve & sleep 10 && ollama pull gemma:2b && wait

EXPOSE 11434

CMD ["ollama", "serve"]