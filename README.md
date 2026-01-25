# Localization Sync Tool

### **Synchronize your translation files and bridge the gap between languages.**

This Python utility is designed to manage of multi-language applications. It compares a **Source** translation file (your most up-to-date version, e.g., English) against multiple **Targofet** files (e.g., Italian, Spanish, French) to identify missing keys.

Instead of manually hunting for what's missing, this tool generates a "ready-to-translate" snippet that you can simply copy-paste into an **LLM (like ChatGPT or Claude)** to complete your localization in seconds.

---

## Key Features

* **Hybrid Parsing:** Reads standard `.json` files and `.js` / `.ts` files using `export const` structures.
* **Deep Extraction:** Uses advanced Regex to capture multi-line strings and various quoting styles (`'` or `"`).
* **LLM-Ready Output:** Generates helper files in the `output/` directory formatted specifically for easy AI translation.
* **Organized Workflow:** Keeps your workspace clean by separating input data from generated results.

---

## 🛠 Prerequisites
- Python 3.x installed on your system.
- No external libraries required (uses built-in `os`, `re`, and `json` modules).
