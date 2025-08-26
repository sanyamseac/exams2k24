# Exams 2k24

This repository contains question papers of the quizzes, endsem and
midsem examinations conducted so far for UG1, year 2024, at IIITH.

## Repository Structure

The repository is structured as follows:

```
exams2k24/
├── <semester>/
│  └── <subject>/
│     ├── Quizzes/
│     ├── Midsems/
│     └── Endsems/
├── contributing.md
└── readme.md
```

All papers are either scanned, or re-written in Markdown and LaTex and
then converted to PDFs. A guide to writing the paper in Markdown/LaTex
can be found in the [contributing guide](contributing.md).

## Contributing to iiitprevpapers Repository

This repository also provides tools to convert papers to the format used by the
[iiitprevpapers repository](https://github.com/VijayrajS/iiitprevpapers), which
maintains a comprehensive collection of previous year papers from IIITH.

To convert papers for contribution to iiitprevpapers:

1. **Run the conversion script:**
   ```bash
   python3 convert_to_iiitprevpapers.py --output converted-papers
   ```

2. **Review the converted structure** in the output directory, which follows
   the iiitprevpapers naming conventions and directory structure.

3. **Fork the [iiitprevpapers repository](https://github.com/VijayrajS/iiitprevpapers)**
   and copy relevant files to contribute them to the broader IIITH community.

The conversion script automatically maps subjects to appropriate abbreviations,
converts exam types to the expected format, and organizes files by year and course type.

> The contents of this repository are intended to be used only for
> reference/practice.
