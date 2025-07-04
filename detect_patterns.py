import os
import re

# Define patterns for failure detection
patterns = {
    "hallucinated_precision": re.compile(r"\d+\.\d{4,}"),  # overly precise decimal
    "fake_quote": re.compile(r'"[^"]+"\s*,?\s*(?:–|-|—)?\s*[^.]*Einstein', re.IGNORECASE),
    "bad_miles_to_km": re.compile(r"(?i)(?:5\s*miles).+?(?:1\.5).+?(?:kilometers)")
}

def detect_failures_in_text(text):
    failures = []
    if patterns["hallucinated_precision"].search(text):
        failures.append("Potential hallucinated precision (too many decimals).")
    if patterns["fake_quote"].search(text):
        failures.append("Possible fake Einstein quote.")
    if patterns["bad_miles_to_km"].search(text):
        failures.append("Likely incorrect miles-to-km conversion.")
    return failures

def main():
    # Loop over all .txt files in the current folder
    for filename in os.listdir():
        if filename.endswith(".txt"):
            print(f"\n📄 Analyzing {filename}:")
            with open(filename, "r", encoding="utf-8") as f:
                text = f.read()
                failures = detect_failures_in_text(text)
                if failures:
                    for f in failures:
                        print(f"  - {f}")
                else:
                    print("  ✓ No known issues detected.")

if __name__ == "__main__":
    main()
