# README.md

# PDF Processor Script

**Project Overview:**
A professional-grade, modular Python project to manage PDF operations including merge, split, and rotate. Structured for cloud-friendly deployment, recruiter-ready portfolio showcase, and easy scalability.

## Features

* Merge multiple PDFs into one file
* Split single PDFs into separate pages
* Rotate PDFs by configurable angles
* Centralized logging with rotation
* YAML-based configuration with Pydantic validation
* Clear error handling with custom exceptions
* CLI with subcommands for user-friendly interaction
* Modular structure for testing and maintenance

## Folder Structure

```
pdf_processor_script/
├── config/
├── core/
├── cli/
├── utils/
├── tests/
├── docs/
├── main.py
├── requirements.txt
├── .gitignore
├── LICENSE
└── legacy/
```

## Installation

```
pip install -r requirements.txt
```

## Usage

```
python main.py merge --input file1.pdf file2.pdf --output merged.pdf
python main.py split --input merged.pdf --output outputs/
python main.py rotate --input merged.pdf --output rotated.pdf --angle 90
```

## Future Enhancements

* Add dry-run mode
* Support for encrypted PDFs
* Web-based UI
* Async PDF processing

## Testing

```
pytest tests/
```

## License

MIT License
