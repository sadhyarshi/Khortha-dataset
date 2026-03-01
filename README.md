# Khortha Multi-Script Dataset

An open-source parallel corpus for the **Khortha language**, featuring mappings between **Devanagari** and **Roman** scripts, with future support for **Anshul Lipi**.

## 📖 Overview
Khortha is a primary language spoken in the Jharkhand region of India. This project aims to create a high-quality, standardized dataset to support Natural Language Processing (NLP) tasks such as machine translation, transliteration, and speech recognition for this low-resource language.

## 📂 Project Structure
- `data/`: Contains the master dataset in CSV format (`khortha_parallel.csv`).
- `scripts/`: Automation tools for script conversion and data cleaning.
- `docs/`: Linguistic guidelines, grammar rules, and script mapping logic.
- `assets/`: Reference materials, including fonts for Anshul Lipi and PDFs.

## 🛠️ Tech Stack
- **Data:** CSV / JSON
- **Automation:** Python (Pandas, Indic-Transliteration)
- **Version Control:** Git & GitHub

## 🚀 Getting Started
### 1. Clone the repository
```bash
git clone [https://github.com/sadhyarshi/Khortha-dataset.git](https://github.com/sadhyarshi/Khortha-dataset.git)
cd Khortha-dataset

Set up the environment
python -m venv venv
.\venv\Scripts\Activate
pip install -r requirements.txt

Run Transliteration
python scripts/generate_roman.py

⚖️ License
This project is licensed under the MIT License - see the LICENSE file for details.

🤝 Contributing
Contributions are welcome! If you are a native speaker or a linguist:

Fork the repo.

Add Khortha sentences in Devanagari to data/khortha_parallel.csv.

Submit a Pull Request.


---