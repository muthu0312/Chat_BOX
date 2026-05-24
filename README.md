# Simple NVIDIA AI Chat Box

This is a beginner-friendly Streamlit chat box for students. It uses the NVIDIA API with the OpenAI Python client.

## 1. Clone The Project

Use the GitHub repository link given by your teacher.

Example:

```powershell
git clone https://github.com/muthu0312/Chat_BOX.git
cd Chat_BOX
```

If your repository name is different, replace `Chat_BOX` with your repository name.

## 2. Create A Virtual Environment

Windows PowerShell:

```powershell
python -m venv venv
```

Activate it:

```powershell
.\venv\Scripts\activate
```

After activation, you should see `(venv)` in the terminal.

If `python` does not work, try:

```powershell
py -m venv venv
.\venv\Scripts\activate
```

## 3. Install Requirements

```powershell
pip install -r requirements.txt
```

## 4. Create The Environment File

Create a file named `.env` in the project folder.

You can copy the example file:

```powershell
copy .env.example .env
```

Open `.env` and add your NVIDIA API key:

```env
NVIDIA_API_KEY=your_nvidia_api_key_here
```

Important: Do not upload `.env` to GitHub. It contains your secret API key.

## 5. Run The App

```powershell
streamlit run app.py
```

Streamlit will show a local URL like:

```text
http://localhost:8501
```

Open that link in your browser.

## How The Code Works

- `st.chat_input()` takes the student's question.
- `st.session_state.messages` remembers the conversation.
- `OpenAI(base_url=...)` connects to NVIDIA's OpenAI-compatible API.
- `client.chat.completions.create()` sends the messages to NVIDIA.
- `st.chat_message()` displays the user and assistant messages.

## Common Problems

If activation is blocked in PowerShell, run:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

Then activate again:

```powershell
.\venv\Scripts\activate
```

If packages are missing, make sure the virtual environment is active and run:

```powershell
pip install -r requirements.txt
```
