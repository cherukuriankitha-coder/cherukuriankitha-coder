"""Small helper that documents the technical areas represented in this portfolio."""
PROJECTS = {
    "hospital-management-system": ["Python", "Pandas", "Machine Learning"],
    "QA-Automation-Portfolio": ["Python", "Selenium", "API Testing", "SQL"],
    "pharmarag-intelligence": ["Python", "OCR", "RAG", "FAISS", "Gradio"],
    "financial-data-analytics": ["Python", "SQL", "Pandas", "Power BI"],
    "sales-performance-analytics": ["Python", "SQL", "Power BI"],
    "customer-churn-prediction": ["Python", "scikit-learn", "Machine Learning"],
    "etl-data-pipeline": ["Python", "SQL", "ETL"],
    "data-quality-framework": ["Python", "SQL", "Data Quality"],
    "job-market-analytics": ["Python", "Pandas", "Analytics"],
}

def projects_using(skill: str):
    skill_lower = skill.lower()
    return [name for name, skills in PROJECTS.items() if any(s.lower() == skill_lower for s in skills)]

if __name__ == "__main__":
    print("Python projects:", projects_using("Python"))
