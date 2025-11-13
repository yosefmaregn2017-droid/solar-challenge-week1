# solar-challenge-week1

**Author:** Yosef Maregn  
**Description:** Template repository for Week 1 - Solar Data Discovery challenge (10 Academy).

## Suggested structure
├── .github/
│   └── workflows/
│       └── ci.yml
├── .gitignore
├── requirements.txt
├── README.md
├── src/
│   └── __init__.py
├── notebooks/
│   ├── benin_eda.ipynb
│   ├── sierraleone_eda.ipynb
│   └── togo_eda.ipynb
├── app/
│   └── main.py
├── tests/
│   └── __init__.py
└── data/   # ignored - keep CSVs local

## Quickstart (local)
```bash
python -m venv .venv
# mac/linux
source .venv/bin/activate
# windows powershell
.\\.venv\\Scripts\\activate

pip install -r requirements.txt
