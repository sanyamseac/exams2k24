# iiitprevpapers Contribution Tools

This directory contains tools to automatically convert the exams2k24 repository structure to the format used by the [iiitprevpapers repository](https://github.com/VijayrajS/iiitprevpapers).

## Quick Start

```bash
# Convert all papers to iiitprevpapers format
python3 convert_to_iiitprevpapers.py --output iiitprevpapers-ready

# The converted files will be in ./iiitprevpapers-ready/
# organized by Year/CourseType/Subject with proper naming
```

## Files

- **`convert_to_iiitprevpapers.py`** - Main conversion script
- **`iiitprevpapers-mapping.json`** - Subject mappings and configuration
- **`IIITPREVPAPERS_GUIDE.md`** - This guide

## Example Output Structure

After conversion, files are organized as:

```
iiitprevpapers-ready/
├── Year1/
│   ├── CS/
│   │   ├── DSA-Data Structures & Algorithms/
│   │   │   ├── DSA_quiz_2024.pdf
│   │   │   ├── DSA_mid1_2024.pdf
│   │   │   └── DSA_end_2024.pdf
│   │   └── ...
│   ├── ECE/
│   └── CLD/
├── Year2/
│   ├── CS/
│   ├── ECE/
│   └── CLD/
└── README.md
```

## How to Contribute to iiitprevpapers

1. **Run the conversion:** `python3 convert_to_iiitprevpapers.py`
2. **Fork** [VijayrajS/iiitprevpapers](https://github.com/VijayrajS/iiitprevpapers)
3. **Copy** relevant files from the conversion output
4. **Create** a pull request

## Customizing Mappings

Edit `iiitprevpapers-mapping.json` to adjust:
- Subject abbreviations
- Course type classifications (CS/ECE/CLD)
- Semester-to-year mappings

## Script Options

```bash
python3 convert_to_iiitprevpapers.py [OPTIONS]

Options:
  --source, -s      Source directory (default: current directory)
  --output, -o      Output directory (default: ./iiitprevpapers-converted)
  --config, -c      Mapping configuration file (default: iiitprevpapers-mapping.json)
  --dry-run         Show what would be done without copying files
  --help           Show help message
```

## Naming Convention

Files are renamed to follow iiitprevpapers format:
- **Pattern:** `<abbr>_<examtype>_2024.pdf`
- **Example:** `DSA_mid1_2024.pdf`
- **Exam types:** quiz, mid1, end
- **Year:** 2024 (for this batch)

This automated approach solves the manual mapping complexity mentioned in the original issue, making it easy to contribute to the broader IIITH papers collection.