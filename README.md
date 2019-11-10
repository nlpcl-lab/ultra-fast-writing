# Simple API

## Requirements

- Python3
- Node.js

# Usage

```bash
cd frontend/
npm install # or yarn add
npm run-script build
cd ../backend/
pip install -r requirements.txt
python -c "import nltk; nltk.download('words'); nltk.download('averaged_perceptron_tagger'); nltk.download('punkt')"
python app.py --init_db # For database initialize
python app.py --port=5678
```
