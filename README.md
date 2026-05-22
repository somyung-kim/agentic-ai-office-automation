# Agentic AI Office Automation

A modular Python project that reads PDF documents, extracts structured information with an LLM-assisted pipeline, and routes the result to Excel or Google Sheets.

This repo is a portfolio project for exploring agentic document automation patterns: document classification, schema-driven extraction, destination routing, OCR fallback, and CLI-based workflows.

> Status: sample PDFs, generated outputs, API keys, and Google service account credentials are intentionally not committed.

---

## Features

- PDF type classification for invoices, application forms, and meeting summaries
- OCR fallback for scanned or image-based PDFs
- Field extraction with Gemini 1.5 Flash
- Schema-driven formatting for structured outputs
- Rule-based routing to Excel or Google Sheets
- Modular pipeline structure with focused extractors, routers, and utilities
- CLI entrypoint for local testing

---

## Supported Document Types

| PDF Type | Format | Output Destination | Key Fields Extracted |
| --- | --- | --- | --- |
| Invoice | Tabular / key-value | Excel (`.xlsx`) | Invoice number, vendor, line items, subtotal, tax, total |
| Application Form | Key-value form | Google Sheets | Name, email, phone, address, education, position |
| Meeting Summary | Paragraph-based | Google Sheets | Title, date, attendees, agenda, action items |

---

## Architecture

The project separates document automation into small pipeline stages:

- `app/utils`: PDF ingestion, OCR/text extraction, document classification, schema helpers
- `app/extractors`: document-specific extraction logic
- `app/agent`: routing and destination selection
- `app/pipelines`: end-to-end workflows per document type
- `app/routers`: Excel and Google Sheets output writers
- `config`: document schemas and routing rules

---

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a local `.env` file:

```bash
cp .env.example .env
```

Add your Gemini API key:

```env
GEMINI_API_KEY=your_api_key_here
```

For Google Sheets output, add a local service account file at:

```text
config/gsheet_service_account.json
```

That file is ignored by Git and should not be committed.

---

## Usage

Run the CLI with a local PDF path:

```bash
python run.py path/to/invoice.pdf --excel_path data/sample_outputs/invoice.xlsx
```

```bash
python run.py path/to/application_form.pdf --sheet_name Application
```

```bash
python run.py path/to/meeting_summary.pdf --sheet_name Meeting_Summary
```

The document type is detected automatically, then routed to the matching pipeline.

---

## Local Development Notes

- Put local PDFs under `data/sample_pdfs/` if you want a staging area.
- Generated Excel outputs can be written under `data/sample_outputs/`.
- Local PDFs, generated outputs, `.env`, and service account credentials are ignored.
- Google Sheets writes require the target spreadsheet to be accessible by the service account.

---

## Technologies

- Python 3.12
- Gemini 1.5 Flash via Google Generative AI
- PyMuPDF, pdfplumber, pdf2image, and Tesseract OCR
- gspread and oauth2client for Google Sheets
- pandas and openpyxl for structured output

---

## Background

See [research.md](./research.md) for the original notes on agentic AI vs. generative AI and why this project is structured as an action-oriented document automation pipeline.

---

## License

MIT License. See [LICENSE](./LICENSE).
