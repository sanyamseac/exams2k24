#!/usr/bin/env python3
"""
Script to convert exams2k24 repository structure to iiitprevpapers repository structure.

This script processes the current repository structure and creates a mapping to the
iiitprevpapers repository format, including proper file renaming and directory structure.
"""

import os
import json
import shutil
import argparse
from pathlib import Path
import re

def load_mapping_config(config_path="iiitprevpapers-mapping.json"):
    """Load the subject mapping configuration."""
    with open(config_path, 'r') as f:
        return json.load(f)

def get_year_from_semester(semester, mapping):
    """Convert semester to year using the mapping."""
    return mapping["semester_to_year"].get(semester, "Unknown")

def get_exam_type(exam_folder, mapping):
    """Convert exam folder name to target exam type."""
    return mapping["exam_type_mapping"].get(exam_folder, exam_folder.lower())

def get_subject_info(subject_name, mapping):
    """Get subject abbreviation, full name, and course type."""
    subject_info = mapping["subject_mappings"].get(subject_name)
    if not subject_info:
        # Generate fallback abbreviation
        words = subject_name.split()
        abbr = ''.join(word[0].upper() for word in words if word)
        return {
            "abbreviation": abbr,
            "full_name": subject_name,
            "course_type": "CS"  # Default to CS
        }
    return subject_info

def sanitize_filename(filename):
    """Remove/replace invalid characters from filename."""
    # Remove or replace characters that might cause issues
    filename = re.sub(r'[<>:"/\\|?*]', '_', filename)
    filename = re.sub(r'\s+', '_', filename)
    return filename

def convert_repository(source_dir, output_dir, config):
    """Convert the entire repository structure."""
    source_path = Path(source_dir)
    output_path = Path(output_dir)
    
    # Create output directory
    output_path.mkdir(parents=True, exist_ok=True)
    
    conversion_log = []
    
    # Process each semester
    for semester_dir in source_path.iterdir():
        if not semester_dir.is_dir() or semester_dir.name.startswith('.'):
            continue
            
        semester_name = semester_dir.name
        if semester_name not in config["semester_to_year"]:
            print(f"Warning: Unknown semester '{semester_name}', skipping...")
            continue
            
        year = get_year_from_semester(semester_name, config)
        print(f"Processing {semester_name} -> {year}")
        
        # Process each subject in the semester
        for subject_dir in semester_dir.iterdir():
            if not subject_dir.is_dir():
                continue
                
            subject_name = subject_dir.name
            subject_info = get_subject_info(subject_name, config)
            
            abbr = subject_info["abbreviation"]
            full_name = subject_info["full_name"]
            course_type = subject_info["course_type"]
            
            print(f"  Processing subject: {subject_name} -> {abbr}")
            
            # Create target directory structure
            target_subject_dir = output_path / year / course_type / f"{abbr}-{full_name}"
            target_subject_dir.mkdir(parents=True, exist_ok=True)
            
            # Process each exam type folder
            for exam_type_dir in subject_dir.iterdir():
                if not exam_type_dir.is_dir():
                    continue
                    
                exam_type = exam_type_dir.name
                target_exam_type = get_exam_type(exam_type, config)
                
                print(f"    Processing exam type: {exam_type} -> {target_exam_type}")
                
                # Process each file in the exam type folder
                for file_path in exam_type_dir.iterdir():
                    if file_path.is_file() and file_path.suffix.lower() == '.pdf':
                        original_filename = file_path.name
                        
                        # Generate new filename: ABBR_examtype_2024.pdf
                        new_filename = f"{abbr}_{target_exam_type}_2024.pdf"
                        
                        # Handle multiple files of same type (add numbers)
                        counter = 1
                        base_new_filename = new_filename
                        while (target_subject_dir / new_filename).exists():
                            name_part = base_new_filename.replace('.pdf', '')
                            new_filename = f"{name_part}_{counter}.pdf"
                            counter += 1
                        
                        new_filename = sanitize_filename(new_filename)
                        target_file_path = target_subject_dir / new_filename
                        
                        # Copy the file
                        shutil.copy2(file_path, target_file_path)
                        
                        conversion_log.append({
                            "original_path": str(file_path.relative_to(source_path)),
                            "new_path": str(target_file_path.relative_to(output_path)),
                            "semester": semester_name,
                            "year": year,
                            "subject": subject_name,
                            "course_type": course_type,
                            "abbreviation": abbr,
                            "exam_type": exam_type,
                            "target_exam_type": target_exam_type
                        })
                        
                        print(f"      {original_filename} -> {new_filename}")
    
    # Save conversion log
    log_file = output_path / "conversion_log.json"
    with open(log_file, 'w') as f:
        json.dump(conversion_log, f, indent=2)
    
    print(f"\nConversion complete! Files copied to: {output_path}")
    print(f"Conversion log saved to: {log_file}")
    print(f"Total files converted: {len(conversion_log)}")
    
    return conversion_log

def generate_readme(output_dir, conversion_log):
    """Generate a README file explaining the conversion."""
    output_path = Path(output_dir)
    readme_content = f"""# Converted Papers for iiitprevpapers Repository

This directory contains papers from the exams2k24 repository converted to match the structure and naming conventions of the [iiitprevpapers repository](https://github.com/VijayrajS/iiitprevpapers).

## Conversion Summary

- **Total files converted**: {len(conversion_log)}
- **Source repository**: sanyamseac/exams2k24
- **Target format**: VijayrajS/iiitprevpapers

## Directory Structure

The files are organized as follows:
```
Year1/Year2/Year3/Year4/
├── CS/              # Computer Science courses
├── ECE/             # Electronics and other engineering courses  
├── CLD/             # Computational Linguistics and other humanities courses
```

## File Naming Convention

Files follow the iiitprevpapers naming convention:
```
<abbr>_<examtype>_2024.pdf
```

Where:
- `<abbr>` is the subject abbreviation
- `<examtype>` is one of: quiz1, quiz2, mid1, mid2, end
- Year is 2024 (the year these papers are from)

## How to Contribute to iiitprevpapers

1. Fork the [iiitprevpapers repository](https://github.com/VijayrajS/iiitprevpapers)
2. Copy the relevant files from this converted structure to the appropriate directories
3. Make sure file names follow the exact convention
4. Create a pull request

## Mapping Details

See `conversion_log.json` for detailed mapping of each file from original location to target location.

## Notes

- All files are from the 2024 academic year (UG1 batch)
- Some subject abbreviations may need adjustment based on existing conventions in the target repository
- Please verify course classifications (CS/ECE/CLD) before contributing
"""

    readme_file = output_path / "README.md"
    with open(readme_file, 'w') as f:
        f.write(readme_content)
    
    print(f"README generated: {readme_file}")

def main():
    parser = argparse.ArgumentParser(description="Convert exams2k24 structure to iiitprevpapers format")
    parser.add_argument("--source", "-s", default=".", help="Source directory (default: current directory)")
    parser.add_argument("--output", "-o", default="./iiitprevpapers-converted", help="Output directory")
    parser.add_argument("--config", "-c", default="iiitprevpapers-mapping.json", help="Mapping configuration file")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be done without actually copying files")
    
    args = parser.parse_args()
    
    # Load configuration
    if not os.path.exists(args.config):
        print(f"Error: Configuration file '{args.config}' not found!")
        return 1
    
    config = load_mapping_config(args.config)
    
    if args.dry_run:
        print("DRY RUN MODE - No files will be copied")
        print(f"Source: {args.source}")
        print(f"Output: {args.output}")
        print(f"Config: {args.config}")
        # TODO: Implement dry run logic
        return 0
    
    # Perform conversion
    try:
        conversion_log = convert_repository(args.source, args.output, config)
        generate_readme(args.output, conversion_log)
        print("\nConversion completed successfully!")
        return 0
    except Exception as e:
        print(f"Error during conversion: {e}")
        return 1

if __name__ == "__main__":
    exit(main())