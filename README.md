# Streamlit Dashboard

This is a simple Streamlit dashboard ready to be deployed on [Render.com](https://render.com/), using [uv](https://github.com/astral-sh/uv) as the package manager.

## Local Development

1. **Install uv** (if not already installed):
   ```sh
   pip install uv
   ```
2. **Create and activate a virtual environment:**
   ```sh
   uv venv
   source .venv/bin/activate
   ```
3. **Install dependencies:**
   ```sh
   uv pip install -r requirements.txt  # or use `uv pip install streamlit` if you want to add more packages
   ```
4. **Run the dashboard:**
   ```sh
   streamlit run dashboard.py
   ```

## Deployment on Render.com

1. **Create a new Web Service** on Render.com.
2. **Set the build and start commands:**
   - **Build Command:**
     ```sh
     uv pip install -r requirements.txt
     ```
   - **Start Command:**
     ```sh
     streamlit run dashboard.py --server.port $PORT --server.address 0.0.0.0
     ```
3. **Add a `requirements.txt` file** (Render.com expects this):
   ```sh
   uv pip freeze > requirements.txt
   ```
4. **Deploy!**

## Notes
- Make sure your `requirements.txt` is up to date with your dependencies.
- The dashboard will be available at the URL provided by Render.com after deployment.