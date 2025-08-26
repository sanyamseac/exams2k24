# Contributing Guide

Thank you for your interest in contributing to this repository of
papers! You can contribute in the following ways:

1. Scanning/re-writing papers and uploading them to the repository.
2. Reporting and correcting mistakes in papers uploaded to the
   repository.
3. Contributing papers to the broader IIITH community via the
   [iiitprevpapers repository](https://github.com/VijayrajS/iiitprevpapers).

## Scanning/Re-writing Papers

If a hardcopy of the paper is distributed, please upload a legible scan
to the repository via a pull request.

If not, then please write a markdown file and use
[this tool](https://github.com/gamemaker1/latex-md-to-html) to convert
it to a PDF.

- Here is a
  [guide to using Markdown](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax).
- Here is a
  [guide to using MathJax](https://math.meta.stackexchange.com/questions/5020/mathjax-basic-tutorial-and-quick-reference)
  to write mathematical expressions.

## Contributing to iiitprevpapers Repository

The [iiitprevpapers repository](https://github.com/VijayrajS/iiitprevpapers) 
maintains a comprehensive collection of previous year papers from IIITH across
all courses and semesters. To help the broader IIITH community, you can
contribute the 2024 papers from this repository to iiitprevpapers.

### Automated Conversion Process

This repository includes an automated conversion tool that handles the complex
mapping and renaming required for iiitprevpapers:

1. **Run the conversion script:**
   ```bash
   python3 convert_to_iiitprevpapers.py --output iiitprevpapers-ready
   ```

2. **Review the output:** The script will create a directory structure matching
   iiitprevpapers conventions with properly renamed files.

3. **Contribute to iiitprevpapers:**
   - Fork the [iiitprevpapers repository](https://github.com/VijayrajS/iiitprevpapers)
   - Copy the relevant files from the converted directory
   - Create a pull request

### Manual Mapping (if needed)

The conversion script uses `iiitprevpapers-mapping.json` for subject mappings.
If you need to adjust mappings:

- **Subject abbreviations:** Check existing abbreviations in iiitprevpapers
- **Course classifications:** Ensure subjects are classified correctly (CS/ECE/CLD)
- **File naming:** Follow the pattern `<abbr>_<examtype>_2024.pdf`

### Important Notes

- Files must be in PDF format only
- Follow the strict naming convention: `<abbr>_<examtype>_<year>.pdf`
- Organize files under the correct Year/CourseType/Subject directory
- Include answer keys as `<abbr>_<examtype>_<year>_key.pdf` if available

## Reporting/Correcting Mistakes

Please open issue to do this by going to
[the issues page](https://github.com/sanyamseac/exams2k24/issues/choose).
