# Student Setup Instructions

## Step 1: Clone

```powershell
git clone https://github.com/muthu0312/Chat_BOX.git
cd Chat_BOX
```

## Step 2: Create Virtual Environment

```powershell
python -m venv venv
```

## Step 3: Activate Virtual Environment

```powershell
.\venv\Scripts\activate
```

## Step 4: Install Requirements

```powershell
pip install -r requirements.txt
```

## Step 5: Create `.env`

```powershell
copy .env.example .env
```

Open `.env` and add:

```env
NVIDIA_API_KEY=your_nvidia_api_key_here
```

## Step 6: Run

```powershell
streamlit run app.py
```

Open the browser link shown in the terminal.
