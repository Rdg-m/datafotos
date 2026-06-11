# DataFotos

A Python utility to automatically rename folders based on the oldest photo's date found within them.

## Description

This tool scans a folder and all its subfolders for image files, extracts the creation date from their EXIF metadata, finds the oldest photo, and renames the main folder with that date in `YYYY-MM-DD` format.

## Features

- Recursively scans folders for image files
- Extracts creation dates from EXIF metadata (supports JPEG and PNG)
- Automatically renames folder with the oldest photo's date
- Skips folders that already have a date prefix
- Verbose mode for detailed output

## Requirements

- Python 3.7+
- Pillow (PIL)

## Installation

```bash
pip install Pillow
```

## Usage

```bash
python datafotos -p /path/to/folder
```

### Options

- `-p, --path` (required): Path to the folder to rename
- `-v, --verbose`: Enable verbose output to see details about scanned files and dates

### Examples

```bash
# Basic usage
python datafotos -p /home/images/vacation

# With verbose output
python datafotos -p /home/images/vacation --verbose

# Rename folder with date prefix added
# Before: /home/images/vacation
# After:  /home/images/2026-03-08 vacation
```

## How It Works

1. Scans all files in the given folder and subfolders
2. Attempts to extract EXIF metadata from each image
3. Looks for DateTimeOriginal, DateTimeDigitized, or DateTime fields
4. Finds the oldest date among all images
5. Renames the folder by prepending the date in `YYYY-MM-DD` format
6. Skips execution if folder already has a date prefix
