import argparse
import os
import sys

# Make project root available for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.utils.pdf_utils import ingest_pdf, extract_text_non_form
from app.extractors.application_form import extract_application_fields
from app.extractors.invoice import extract_invoice_fields
from app.extractors.meeting_summary import extract_meeting_fields


def main():
    parser = argparse.ArgumentParser(
        description="Test PDF extraction: layout or form fields."
    )
    parser.add_argument("pdf_path", help="Path to the PDF file to extract text from.")
    parser.add_argument(
        "--method",
        choices=["text_layout", "invoice", "application", "meeting_summary"],
        required=True,
        help="Extraction method: 'text_layout', 'invoice', 'application', or 'meeting_summary'",
    )
    args = parser.parse_args()

    print(f"📥 Ingesting: {args.pdf_path}")
    copied_path = ingest_pdf(args.pdf_path)

    print(f"📄 Extracting using method: {args.method}")
    if args.method == "text_layout":
        extracted = extract_text_non_form(copied_path)
    elif args.method == "invoice":
        extracted = extract_invoice_fields(copied_path)
    elif args.method == "application":
        extracted = extract_application_fields(copied_path)
    elif args.method == "meeting_summary":
        extracted = extract_meeting_fields(copied_path)

    print("\n--- Extracted Text ---\n")
    if not isinstance(extracted, dict):
        print(extracted if extracted else "[NO TEXT FOUND]")
    else:
        print("\n".join([f"{k}: {v}" for k, v in extracted.items()]))


if __name__ == "__main__":
    main()
