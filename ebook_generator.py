#!/usr/bin/env python3
"""
Ebook Generator for Regtech Guide

This script uses pandoc to generate a single-page ebook and PDF from the book chapters.
It combines all chapters into a single document with proper formatting and metadata.
"""

import os
import sys
import subprocess
import logging
from pathlib import Path
from typing import List, Optional
import yaml

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('ebook_generator.log'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

class EbookGenerator:
    def __init__(self, project_root: str = "."):
        self.project_root = Path(project_root)
        self.book_dir = self.project_root / "book"
        self.output_dir = self.project_root / "output"
        self.metadata_file = self.project_root / "metadata.yaml"        
        self.overview_file = self.book_dir / "Book_Overview.md"
        
        # Create output directory if it doesn't exist
        self.output_dir.mkdir(exist_ok=True)

    def check_dependencies(self) -> bool:
        """Check if required dependencies are available."""
        try:
            # Check if pandoc is installed
            result = subprocess.run(['pandoc', '--version'], 
                                  capture_output=True, text=True, timeout=10)
            if result.returncode != 0:
                logger.error("Pandoc is not installed or not accessible")
                return False
            
            logger.info(f"Pandoc version: {result.stdout.split()[1]}")
            return True
            
        except (subprocess.TimeoutExpired, FileNotFoundError) as e:
            logger.error(f"Error checking pandoc: {e}")
            return False

    def get_chapter_files(self) -> List[Path]:
        """Get list of chapter files in correct order."""
        chapter_files = []
        
        for chapter_path in self.book_dir.glob('Chapter_*.md'):
            chapter_files.append(chapter_path)
        
        def chapter_number(chapter_file: Path) -> int:
            return int(chapter_file.name.split('_')[1])
        
        chapter_files.sort(key=chapter_number)
        
        
        logger.info(f"Found {len(chapter_files)} chapter files")
        return chapter_files

    def create_combined_markdown(self, chapter_files: List[Path]) -> Path:
        """Combine all chapters into a single markdown file."""
        combined_file = self.output_dir / "regtech_guide.md"
        
        logger.info("Creating combined markdown file...")
        
        with open(combined_file, 'w', encoding='utf-8') as outfile:

            logger.info(f"Processing {self.overview_file.name}...")
            if not self.overview_file.exists():
                raise Exception(f"Overview file not found: {self.overview_file}")
                return None
            with open(self.overview_file, 'r', encoding='utf-8') as infile:
                content = infile.read()
            outfile.write(content)
            outfile.write('\n\n\\newpage\n\n')
                        
            for i, chapter_file in enumerate(chapter_files):
                logger.info(f"Processing {chapter_file.name}...")
                
                with open(chapter_file, 'r', encoding='utf-8') as infile:
                    content = infile.read()
                    outfile.write(content)
                    outfile.write('\n\n\\newpage\n\n')
                    outfile.write('\n\n')
                
                # Add page break between chapters (except for first chapter)
                if i > 0:
                    outfile.write('\n\n\\newpage\n\n')
                        
        logger.info(f"Combined markdown created: {combined_file}")
        return combined_file

    def generate_epub(self, combined_file: Path) -> Path:
        """Generate EPUB ebook from combined markdown."""
        logger.info("Generating EPUB...")
        epub_file = self.output_dir / "regtech_guide.epub"
        
        cmd = [
            'pandoc',
            str(combined_file),
            '-o', str(epub_file),
            '--standalone',
            '--toc',
            '--toc-depth=2',
            '--css=styles.css' if (self.project_root / 'styles.css').exists() else '',
            f'--metadata-file={self.metadata_file}',
        ]        
        
        # Remove empty strings from command
        cmd = [arg for arg in cmd if arg]
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            if result.returncode == 0:
                logger.info(f"EPUB generated successfully: {epub_file}")
                return epub_file
            else:
                logger.error(f"EPUB generation failed: {result.stderr}")
                return None
        except subprocess.TimeoutExpired:
            logger.error("EPUB generation timed out")
            return None
        except Exception as e:
            logger.error(f"Error generating EPUB: {e}")
            return None

    def generate_pdf(self, combined_file: Path) -> Path:
        """Generate PDF from combined markdown."""
        logger.info("Generating PDF...")
        pdf_file = self.output_dir / "regtech_guide.pdf"
                            
        cmd = [
            'pandoc',
            str(combined_file),
            '-o', str(pdf_file),
            '--pdf-engine=mactex',
            '--toc',
            '--toc-depth=2',
            '--number-sections',
            '--highlight-style=tango',
            # '--geometry=margin=2.5cm',
            # '--fontsize=11pt',
            # '--documentclass=book',
            f'--metadata-file={self.metadata_file}',
        ]
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
            if result.returncode == 0:
                logger.info(f"PDF generated successfully: {pdf_file}")
                return pdf_file
            else:
                logger.error(f"PDF generation failed: {result.stderr}")
                return None
        except subprocess.TimeoutExpired:
            logger.error("PDF generation timed out")
            return None
        except Exception as e:
            logger.error(f"Error generating PDF: {e}")
            return None


    def generate_html(self, combined_file: Path) -> Path:
        """Generate HTML version from combined markdown."""
        logger.info("Generating HTML...")
        html_file = self.output_dir / "regtech_guide.html"
        
        cmd = [
            'pandoc',
            str(combined_file),
            '-o', str(html_file),
            '--standalone',
            '--toc',
            '--toc-depth=3',
            '--number-sections',
            '--shift-heading-level-by=1',
            '--css=styles.css' if (self.project_root / 'styles.css').exists() else '',
            f'--metadata-file={self.metadata_file}',
        ]
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            if result.returncode == 0:
                logger.info(f"HTML generated successfully: {html_file}")
                return html_file
            else:
                logger.error(f"HTML generation failed: {result.stderr}")
                return None
        except subprocess.TimeoutExpired:
            logger.error("HTML generation timed out")
            return None
        except Exception as e:
            logger.error(f"Error generating HTML: {e}")
            return None

    def generate_all(self, format: str) -> bool:
        """Generate all ebook formats."""
        logger.info("Starting ebook generation...")
        
        # Check dependencies
        if not self.check_dependencies():
            return False
                
        # Get chapter files
        chapter_files = self.get_chapter_files()
        if not chapter_files:
            logger.error("No chapter files found")
            return False
        
        # Create combined markdown
        combined_file = self.create_combined_markdown(chapter_files)
        if not combined_file:
            return False
        
        # Generate all formats
        success = True

        if format in ['html', 'all']:
            # Generate HTML
            html_file = self.generate_html(combined_file)
            if not html_file:
                success = False

        if format in ['epub', 'all']:  
            # Generate EPUB
            epub_file = self.generate_epub(combined_file)
            if not epub_file:
                success = False
                
        if format in ['pdf', 'all']:
            # Generate PDF
            pdf_file = self.generate_pdf(combined_file)
            if not pdf_file:
                success = False
                
        if success:
            logger.info("All ebook formats generated successfully!")
            logger.info(f"Output directory: {self.output_dir}")
        else:
            logger.error("Some ebook formats failed to generate")
        
        return success


def main():
    """Main function."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Generate Regtech Guide ebooks')
    parser.add_argument('--format', choices=['epub', 'pdf', 'html', 'all'], 
                       default='all', help='Output format to generate')
    parser.add_argument('--project-root', default='.', 
                       help='Project root directory')
    
    args = parser.parse_args()
    
    generator = EbookGenerator(args.project_root)
    
    if args.format == 'all':
        success = generator.generate_all(args.format)
    else:
        # For individual formats, we'd need to implement specific methods
        logger.info(f"Individual format generation not yet implemented: {args.format}")
        success = generator.generate_all()
    
    sys.exit(0 if success else 1)
    

if __name__ == "__main__":
    main()
