# Applied Cryptography Simulator — Online Version

## Run Locally
```bash
pip install streamlit
python -m streamlit run app.py
```

## Deploy Online (Free)
1. Push this folder to a GitHub repository
2. Go to https://share.streamlit.io
3. Sign in with GitHub
4. Click **New app** → select your repo → set main file to `app.py`
5. Click **Deploy** — you get a public URL

## Files
- `app.py` — Web interface
- `cipher.py` — Caesar Cipher logic (same as offline version)
- `hashing.py` — SHA-256 logic (same as offline version)
- `requirements.txt` — dependencies
