"""
app.py — Web app version of the Applied Cryptography Simulator.
"""

import streamlit as st
from cipher import validate_key, encrypt, decrypt
from hashing import verify_integrity

st.set_page_config(
    page_title="Applied Cryptography Simulator",
    layout="wide"
)

st.markdown("""
<style>
    html, body, [data-testid="stAppViewContainer"], [data-testid="stMain"] {
        background-color: #f8fafc !important;
        color: #1e293b;
        font-family: 'Segoe UI', sans-serif;
    }
    [data-testid="stHeader"] { background: transparent !important; }
    .block-container { padding: 2rem 3rem !important; max-width: 1100px; }

    .app-header {
        background: linear-gradient(135deg, #4c1d95, #1e40af);
        border-radius: 10px;
        padding: 1.4rem 2rem;
        margin-bottom: 1.6rem;
    }
    .app-header h1 { color: #fff; font-size: 1.4rem; font-weight: 700; margin: 0 0 0.3rem 0; }
    .app-header p  { color: #ddd6fe; font-size: 0.85rem; margin: 0; letter-spacing: 1.5px; }

    .panel {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        padding: 1.2rem 1.5rem;
        margin-bottom: 1rem;
        box-shadow: 0 1px 4px rgba(0,0,0,0.06);
    }
    .panel-title {
        font-size: 0.75rem;
        font-weight: 700;
        letter-spacing: 2px;
        color: #7c3aed;
        text-transform: uppercase;
        border-bottom: 1px solid #e2e8f0;
        padding-bottom: 0.5rem;
        margin-bottom: 1rem;
    }

    .stTextInput > label {
        color: #475569 !important;
        font-size: 0.8rem !important;
        font-weight: 700 !important;
        letter-spacing: 1px !important;
        text-transform: uppercase !important;
    }
    .stTextInput > div > div > input {
        background: #f8fafc !important;
        color: #1e293b !important;
        border: 1px solid #cbd5e1 !important;
        border-radius: 6px !important;
        font-family: 'Consolas', monospace !important;
        font-size: 1rem !important;
    }
    .stTextInput > div > div > input:focus {
        border-color: #7c3aed !important;
        box-shadow: 0 0 0 2px rgba(124,58,237,0.15) !important;
    }

    .stButton > button {
        background: linear-gradient(135deg, #7c3aed, #2563eb) !important;
        color: #fff !important;
        border: none !important;
        border-radius: 6px !important;
        font-weight: 700 !important;
        font-size: 0.95rem !important;
        letter-spacing: 1.5px !important;
        padding: 0.65rem 2rem !important;
        width: 100% !important;
    }
    .stButton > button:hover { opacity: 0.9; }

    .result-box {
        background: #f1f5f9;
        border: 1px solid #cbd5e1;
        border-radius: 6px;
        padding: 0.8rem 1rem;
        font-family: 'Consolas', monospace;
        font-size: 1rem;
        color: #1e293b;
        word-break: break-all;
        min-height: 2.8rem;
    }
    .hash-box {
        background: #f1f5f9;
        border: 1px solid #cbd5e1;
        border-radius: 6px;
        padding: 0.65rem 1rem;
        font-family: 'Consolas', monospace;
        font-size: 0.78rem;
        color: #6d28d9;
        word-break: break-all;
    }
    .field-label {
        color: #94a3b8;
        font-size: 0.75rem;
        font-weight: 700;
        letter-spacing: 1px;
        text-transform: uppercase;
        margin-bottom: 0.35rem;
    }
    .verified {
        background: #f0fdf4;
        border: 1px solid #86efac;
        border-radius: 6px;
        padding: 0.9rem 1.2rem;
        color: #15803d;
        font-weight: 700;
        font-size: 0.95rem;
    }
    .failed {
        background: #fff1f2;
        border: 1px solid #fca5a5;
        border-radius: 6px;
        padding: 0.9rem 1.2rem;
        color: #b91c1c;
        font-weight: 700;
        font-size: 0.95rem;
    }
    .footer {
        text-align: center;
        color: #94a3b8;
        font-size: 0.75rem;
        margin-top: 2rem;
        letter-spacing: 0.5px;
    }
    #MainMenu, footer, [data-testid="stToolbar"],
    [data-testid="stDecoration"] { display: none !important; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="app-header">
    <h1>[+] Applied Cryptography &amp; Secure Network Protocol Simulator</h1>
    <p>CAESAR CIPHER ENCRYPTION &nbsp;|&nbsp; DECRYPTION &nbsp;|&nbsp; SHA-256 INTEGRITY VERIFICATION</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="panel"><div class="panel-title">[>] Input</div>', unsafe_allow_html=True)
col1, col2 = st.columns([4, 1])
with col1:
    plaintext = st.text_input("Plaintext", placeholder="e.g.  HELLO WORLD")
with col2:
    key_str = st.text_input("Key (integer)", placeholder="e.g.  3")
st.markdown('</div>', unsafe_allow_html=True)

run = st.button("[ RUN ]  Encrypt  ->  Decrypt  ->  Verify Integrity")

if run:
    if not plaintext.strip():
        st.error("[!] Plaintext cannot be empty.")
        st.stop()

    valid, key, err = validate_key(key_str)
    if not valid:
        st.error(f"[!] Key Error: {err}")
        st.stop()

    ciphertext        = encrypt(plaintext, key)
    decrypted         = decrypt(ciphertext, key)
    h_orig, h_dec, ok = verify_integrity(plaintext, decrypted)

    col_l, col_r = st.columns(2)
    with col_l:
        st.markdown(f"""
        <div class="panel">
            <div class="panel-title">[#] Encryption</div>
            <div class="field-label">Ciphertext &nbsp;/&nbsp; Key = {key}</div>
            <div class="result-box">{ciphertext}</div>
        </div>
        """, unsafe_allow_html=True)

    with col_r:
        st.markdown(f"""
        <div class="panel">
            <div class="panel-title">[#] Decryption</div>
            <div class="field-label">Recovered Plaintext</div>
            <div class="result-box">{decrypted}</div>
        </div>
        """, unsafe_allow_html=True)

    integrity_html = (
        '<div class="verified">[OK] VERIFIED — Message integrity is intact. Both hashes match.</div>'
        if ok else
        '<div class="failed">[!!] FAILED — Message integrity has been compromised. Hashes do not match.</div>'
    )
    st.markdown(f"""
    <div class="panel">
        <div class="panel-title">[*] SHA-256 Integrity Verification</div>
        <div class="field-label">Original SHA-256</div>
        <div class="hash-box">{h_orig}</div>
        <br>
        <div class="field-label">Decrypted SHA-256</div>
        <div class="hash-box">{h_dec}</div>
        <br>
        {integrity_html}
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class="footer">
    Applied Cryptography &amp; Secure Network Protocol Simulator &nbsp;|&nbsp; Academic Project &nbsp;|&nbsp; Python
</div>
""", unsafe_allow_html=True)
