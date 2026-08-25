# Applied Cryptography Simulator — Online Version (Streamlit)

## Run Locally
```bash
pip install streamlit
streamlit run app.py
```

## Deploy to Streamlit Cloud (Free)
1. Push this folder to a GitHub repository
2. Go to https://streamlit.io/cloud
3. Sign in with GitHub
4. Click **New app** → select your repo → set main file to `app.py`
5. Click **Deploy** — you get a public URL like `https://your-app.streamlit.app`

## Files
- `app.py` — Streamlit web interface
- `cipher.py` — Caesar Cipher logic (same as offline version)
- `hashing.py` — SHA-256 logic (same as offline version)
- `requirements.txt` — tells Streamlit Cloud to install streamlit
