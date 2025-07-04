import re

def detect_failures(text):
    issues = []

    if "Cl is retained" in text and "Cl is displaced" in text:
        issues.append("❗ Contradiction: Both Cl retained and Cl displaced mentioned.")

    if re.search(r"\$[0-9]+,[0-9]+\.[0-9]{4,}", text):
        issues.append("🔍 Potential hallucinated precision (too many decimals in dollar amount).")

    if "pivot table" in text and "row" in text and "off by one" in text:
        issues.append("⚠ Possible spreadsheet agent failure: row offset error.")

    return issues

if __name__ == "__main__":
    sample_text = open("sample_ai_output.txt").read()
    results = detect_failures(sample_text)
    for r in results:
        print(r)
