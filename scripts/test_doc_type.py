import os
import sys
import argparse

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.utils.pdf_utils import extract_text_non_form
from app.utils.doc_type_detector import get_doc_type


def main():
    parser = argparse.ArgumentParser(
        description="Test document type detection using LLM + fallback."
    )
    parser.add_argument("pdf_path", help="Path to the PDF file.")
    args = parser.parse_args()

    print(f"📄 Reading: {args.pdf_path}")
    text = extract_text_non_form(args.pdf_path)

    print("\n🔍 Detecting document type...\n")
    doc_type = get_doc_type(text)

    print(f"\n📌 Detected Type: {doc_type}")


if __name__ == "__main__":
    main()
