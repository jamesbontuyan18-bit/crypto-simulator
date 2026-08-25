"""
app.py — Web app version of the Applied Cryptography Simulator.

Run locally:
    pip install streamlit
    python -m streamlit run app.py
"""

import streamlit as st
from cipher import validate_key, encrypt, decrypt
from hashing import verify_integrity

st.set_page_config(
    page_title="Applied Cryptography Simulator",
    page_icon="[+]",
    layout="wide"
)

st.markdown("""
<style>
    /* ── Base ── */
    html, body, [data-testid="stAppViewContainer"] {
        background-color: #0f0f1a !important;
        color: #e2e8f0;
        font-family: 'Segoe UI', sans-serif;
    }
    [data-testid="stHeader"] { background: transparent; }
    [data-testid="stSidebar"] { display: none; }
    .block-container {
        padding: 2rem 3rem 2rem 3rem !important;
        max-width: 1100px;
    }

    /* ── Header banner ── */
    .app-header {
        background: linear-gradient(135deg, #3b0764 0%, #1e1b4b 100%);
        border-radius: 10px;
        padding: 1.4rem 2rem;
        margin-bottom: 1.6rem;
        border-left: 5px solid #7c3aed;
    }
    .app-header h1 {
        color: #ffffff;
        font-size: 1.45rem;
        font-weight: 700;
        margin: 0 0 0.3rem 0;
        letter-spacing: 0.3px;
    }
    .app-header p {
        color: #c4b5fd;
        font-size: 0.88rem;
        margin: 0;
        letter-spacing: 1px;
    }

    /* ── Section panels ── */
    .panel {
        background: #1a1a2e;
        border: 1px solid #2a2a4a;
        border-radius: 8px;
        padding: 1.2rem 1.5rem;
        margin-bottom: 1rem;
    }
    .panel-title {
        font-size: 0.78rem;
        font-weight: 700;
        letter-spacing: 2px;
        color: #7c3aed;
        text-transform: uppercase;
        border-bottom: 1px solid #2a2a4a;
        padding-bottom: 0.5rem;
        margin-bottom: 1rem;
    }

    /* ── Input fields ── */
    .stTextInput > label {
        color: #94a3b8 !important;
        font-size: 0.82rem !important;
        font-weight: 600;
        letter-spacing: 0.5px;
    }
    .stTextInput > div > div > input {
        background: #0d0d1a !important;
        color: #e2e8f0 !important;
        border: 1px solid #2a2a4a !important;
        border-radius: 6px !important;
        font-family: 'Consolas', monospace !important;
        font-size: 0.95rem !important;
        padding: 0.5rem 0.75rem !important;
    }
    .stTextInput > div > div > input:focus {
        border-color: #7c3aed !important;
        box-shadow: 0 0 0 2px rgba(124,58,237,0.2) !important;
    }

    /* ── Button ── */
    .stButton > button {
        background: linear-gradient(135deg, #7c3aed, #4f46e5) !important;
        color: white !important;
        border: none !important;
        border-radius: 6px !important;
        font-weight: 700 !important;
        font-size: 0.9rem !important;
        letter-spacing: 1px !important;
        padding: 0.6rem 1.5rem !important;
        transition: opacity 0.2s;
    }
    .stButton > button:hover { opacity: 0.88; }

    /* ── Result boxes ── */
    .result-box {
        background: #0d0d1a;
        border: 1px solid #2a2a4a;
        border-radius: 6px;
        padding: 0.75rem 1rem;
        font-family: 'Consolas', monospace;
        font-size: 1rem;
        color: #e2e8f0;
        word-break: break-all;
        min-height: 2.5rem;
    }
    .hash-box {
        background: #0d0d1a;
        border: 1px solid #2a2a4a;
        border-radius: 6px;
        padding: 0.65rem 1rem;
        font-family: 'Consolas', monospace;
        font-size: 0.78rem;
        color: #a78bfa;
        word-break: break-all;
    }
    .label {
        color: #64748b;
        font-size: 0.78rem;
        font-weight: 600;
        letter-spacing: 0.5px;
        margin-bottom: 0.3rem;
    }

    /* ── Integrity result ── */
    .verified {
        background: #052e16;
        border: 1px solid #166534;
        border-radius: 6px;
        padding: 0.8rem 1.2rem;
        color: #22c55e;
        font-weight: 700;
        font-size: 1rem;
        letter-spacing: 0.5px;
    }
    .failed {
        background: #2d0a0a;
        border: 1px solid #7f1d1d;
        border-radius: 6px;
        padding: 0.8rem 1.2rem;
        color: #ef4444;
        font-weight: 700;
        font-size: 1rem;
        letter-spacing: 0.5px;
    }

    /* ── Footer ── */
    .footer {
        text-align: center;
        color: #334155;
        font-size: 0.75rem;
        margin-top: 2rem;
        letter-spacing: 0.5px;
    }

    /* hide default streamlit chrome */
    #MainMenu, footer, [data-testid="stToolbar"] { display: none; }
    .stAlert { border-radius: 6px !important; }
</style>
""", unsafe_allow_html=True)

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="app-header">
    <h1>[+] Applied Cryptography &amp; Secure Network Protocol Simulator</h1>
    <p>CAESAR CIPHER ENCRYPTION &nbsp;|&nbsp; DECRYPTION &nbsp;|&nbsp; SHA-256 INTEGRITY VERIFICATION</p>
</div>
""", unsafe_allow_html=True)

# ── Input ─────────────────────────────────────────────────────────────────────
st.markdown('<div class="panel"><div class="panel-title">[>] Input</div>', unsafe_allow_html=True)
col1, col2 = st.columns([4, 1])
with col1:
    plaintext = st.text_input("PLAINTEXT", placeholder="e.g.  HELLO WORLD")
with col2:
    key_str = st.text_input("KEY (integer)", placeholder="e.g.  3")
st.markdown('</div>', unsafe_allow_html=True)

# ── Run Button ────────────────────────────────────────────────────────────────
run = st.button("[ RUN ]  Encrypt  ->  Decrypt  ->  Verify Integrity", use_container_width=True)

if run:
    if not plaintext.strip():
        st.error("[!] Plaintext cannot be empty.")
        st.stop()

    valid, key, err = validate_key(key_str)
    if not valid:
        st.error(f"[!] Key Error: {err}")
        st.stop()

    ciphertext = encrypt(plaintext, key)
    decrypted  = decrypt(ciphertext, key)
    h_orig, h_dec, ok = verify_integrity(plaintext, decrypted)

    col_left, col_right = st.columns(2)

    # ── Encryption ────────────────────────────────────────────────────────
    with col_left:
        st.markdown(f"""
        <div class="panel">
            <div class="panel-title">[#] Encryption</div>
            <div class="label">CAESAR CIPHER &nbsp;/&nbsp; KEY = {key}</div>
            <div class="result-box">{ciphertext}</div>
        </div>
        """, unsafe_allow_html=True)

    # ── Decryption ────────────────────────────────────────────────────────
    with col_right:
        st.markdown(f"""
        <div class="panel">
            <div class="panel-title">[#] Decryption</div>
            <div class="label">RECOVERED PLAINTEXT</div>
            <div class="result-box">{decrypted}</div>
        </div>
        """, unsafe_allow_html=True)

    # ── Integrity ─────────────────────────────────────────────────────────
    st.markdown(f"""
    <div class="panel">
        <div class="panel-title">[*] SHA-256 Integrity Verification</div>
        <div class="label">ORIGINAL SHA-256</div>
        <div class="hash-box">{h_orig}</div>
        <br>
        <div class="label">DECRYPTED SHA-256</div>
        <div class="hash-box">{h_dec}</div>
        <br>
        {'<div class="verified">[OK] VERIFIED &mdash; Message integrity is intact. Both hashes match.</div>'
         if ok else
         '<div class="failed">[!!] FAILED &mdash; Message integrity has been compromised. Hashes do not match.</div>'}
    </div>
    """, unsafe_allow_html=True)

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="footer">
    Applied Cryptography &amp; Secure Network Protocol Simulator &nbsp;|&nbsp; Academic Project &nbsp;|&nbsp; Python
</div>
""", unsafe_allow_html=True)
