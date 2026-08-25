"""
app.py — Streamlit web app version of the Applied Cryptography Simulator.

Run locally:
    pip install streamlit
    streamlit run app.py

Deploy:
    Push to GitHub → connect to streamlit.io/cloud → deploy
"""

import streamlit as st
from cipher import validate_key, encrypt, decrypt
from hashing import verify_integrity

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Applied Cryptography Simulator",
    page_icon="🔐",
    layout="centered"
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
    .main { background-color: #1e1e2e; }
    .block-container { padding-top: 1.5rem; }
    .stTextInput > label, .stNumberInput > label { color: #94a3b8; font-size: 0.9rem; }
    .hash-box {
        background: #12121f;
        border-radius: 6px;
        padding: 10px 14px;
        font-family: monospace;
        font-size: 0.82rem;
        word-break: break-all;
        color: #a78bfa;
        border: 1px solid #2a2a3e;
    }
    .result-box {
        background: #12121f;
        border-radius: 6px;
        padding: 10px 14px;
        font-family: monospace;
        font-size: 1rem;
        color: #e2e8f0;
        border: 1px solid #2a2a3e;
    }
    .verified   { color: #22c55e; font-weight: bold; font-size: 1.1rem; }
    .failed     { color: #ef4444; font-weight: bold; font-size: 1.1rem; }
    .section-title { color: #a78bfa; font-weight: 600; margin-bottom: 0.2rem; }
</style>
""", unsafe_allow_html=True)

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown("## 🔐 Applied Cryptography & Secure Network Protocol Simulator")
st.markdown("*Caesar Cipher Encryption &nbsp;•&nbsp; Decryption &nbsp;•&nbsp; SHA-256 Integrity Verification*")
st.divider()

# ── Input Section ─────────────────────────────────────────────────────────────
st.markdown('<p class="section-title">📝 INPUT</p>', unsafe_allow_html=True)

col1, col2 = st.columns([3, 1])
with col1:
    plaintext = st.text_input("Plaintext", placeholder="e.g. HELLO WORLD")
with col2:
    key_str = st.text_input("Encryption Key", placeholder="e.g. 3")

st.divider()

# ── Run All Button ────────────────────────────────────────────────────────────
run = st.button("⚡ Run All Steps  (Encrypt → Decrypt → Verify)", use_container_width=True, type="primary")

if run:
    # Validate
    if not plaintext.strip():
        st.error("⚠️ Plaintext cannot be empty.")
        st.stop()

    valid, key, err = validate_key(key_str)
    if not valid:
        st.error(f"⚠️ Key Error: {err}")
        st.stop()

    # Encrypt
    ciphertext = encrypt(plaintext, key)

    # Decrypt
    decrypted = decrypt(ciphertext, key)

    # Integrity
    h_orig, h_dec, ok = verify_integrity(plaintext, decrypted)

    # ── Encryption Result ─────────────────────────────────────────────────
    st.markdown('<p class="section-title">🔒 ENCRYPTION</p>', unsafe_allow_html=True)
    st.caption(f"Caesar Cipher applied with key = {key}")
    st.markdown(f'<div class="result-box">{ciphertext}</div>', unsafe_allow_html=True)

    st.divider()

    # ── Decryption Result ─────────────────────────────────────────────────
    st.markdown('<p class="section-title">🔓 DECRYPTION</p>', unsafe_allow_html=True)
    st.caption("Ciphertext reversed back to plaintext")
    st.markdown(f'<div class="result-box">{decrypted}</div>', unsafe_allow_html=True)

    st.divider()

    # ── Integrity Section ─────────────────────────────────────────────────
    st.markdown('<p class="section-title">🛡️ SHA-256 INTEGRITY VERIFICATION</p>', unsafe_allow_html=True)

    st.caption("Original SHA-256")
    st.markdown(f'<div class="hash-box">{h_orig}</div>', unsafe_allow_html=True)

    st.caption("Decrypted SHA-256")
    st.markdown(f'<div class="hash-box">{h_dec}</div>', unsafe_allow_html=True)

    st.markdown("")
    if ok:
        st.markdown('<p class="verified">✅ VERIFIED — Message integrity is intact</p>',
                    unsafe_allow_html=True)
        st.success("Both SHA-256 hashes match. The encryption/decryption round-trip was lossless.")
    else:
        st.markdown('<p class="failed">❌ FAILED — Message integrity has been compromised</p>',
                    unsafe_allow_html=True)
        st.error("Hashes do not match. The message was altered or an incorrect key was used.")

# ── Footer ────────────────────────────────────────────────────────────────────
st.divider()
st.caption("Applied Cryptography & Secure Network Protocol Simulator — Academic Project · Python + Streamlit")
