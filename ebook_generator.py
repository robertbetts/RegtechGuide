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
        logging.FileHandler('ebook_generation.log'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

class EbookGenerator:
    def __init__(self, project_root: str = "."):
        self.project_root = Path(project_root)
        self.book_dir = self.project_root / "book"
        self.output_dir = self.project_root / "output"
        self.metadata_file = self.project_root / "book" / "metadata.yaml"
        
        # Create output directory if it doesn't exist
        self.output_dir.mkdir(exist_ok=True)


        self.overview_file = self.book_dir / "overview.md"
        self.contents_file = self.book_dir / "Contents.md"
        
        # Define chapter order based on overview_and_contents.md
        self.chapter_order = [
            "Chapter_01_introduction_to_regulatory_technology.md",
            "Chapter_02_regulatory_landscape_and_frameworks.md",
            "Chapter_03_the_business_case_for_regtech.md",
            "Chapter_04_software_engineering_for_regulated_environments.md",
            "Chapter_05_architecture_patterns_for_compliance.md",
            "Chapter_06_data_management_and_governance.md",
            "Chapter_07_security_and_privacy_by_design.md",
            "Chapter_08_change_management_in_regulated_environments.md",
            "Chapter_09_monitoring_observability_and_compliance.md",
            "Chapter_10_testing_and_quality_assurance.md",
            "Chapter_11_incident_response_and_business_continuity.md",
            "Chapter_12_financial_services_regtech.md",
            "Chapter_13_healthcare_and_life_sciences.md",
            "Chapter_14_data_protection_and_privacy.md",
            "Chapter_15_energy_and_environmental_compliance.md",
            "Chapter_16_artificial_intelligence_and_machine_learning_in_regtech.md",
            "Chapter_17_blockchain_and_distributed_ledger_technology.md",
            "Chapter_18_cloud_computing_and_regulatory_compliance.md",
            "Chapter_19_api_management_and_integration.md",
            "Chapter_20_risk_management_frameworks.md",
            "Chapter_21_audit_and_examination_readiness.md",
            "Chapter_22_vendor_management_and_third_party_risk.md",
            "Chapter_23_regulatory_reporting_and_documentation.md",
            "Chapter_24_regulatory_sandboxes_and_innovation.md",
            "Chapter_25_cross_border_compliance_and_international_standards.md",
            "Chapter_26_the_future_of_regtech.md"
        ]

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

    def load_metadata(self) -> Optional[dict]:
        """Load metadata from YAML file."""
        if not self.metadata_file.exists():
            logger.warning(f"Metadata file not found: {self.metadata_file}")
            return None
            
        try:
            with open(self.metadata_file, 'r', encoding='utf-8') as f:
                metadata = yaml.safe_load(f)
            logger.info("Metadata loaded successfully")
            return metadata
        except Exception as e:
            logger.error(f"Error loading metadata: {e}")
            return None

    def get_chapter_files(self) -> List[Path]:
        """Get list of chapter files in correct order."""
        chapter_files = []
        
        for chapter_name in self.chapter_order:
            chapter_path = self.book_dir / chapter_name
            if chapter_path.exists():
                chapter_files.append(chapter_path)
            else:
                logger.warning(f"Chapter file not found: {chapter_path}")
        
        logger.info(f"Found {len(chapter_files)} chapter files")
        return chapter_files

    def create_combined_markdown(self, chapter_files: List[Path]) -> Path:
        """Combine all chapters into a single markdown file."""
        combined_file = self.output_dir / "regtech_guide_combined.md"
        
        logger.info("Creating combined markdown file...")
        
        with open(combined_file, 'w', encoding='utf-8') as outfile:

            with open(self.overview_file, 'r', encoding='utf-8') as infile:
                content = infile.read()
            outfile.write(content)
            outfile.write('\n\n\\newpage\n\n')
            
            with open(self.contents_file, 'r', encoding='utf-8') as infile:
                content = infile.read()
            outfile.write(content)
            outfile.write('\n\n\\newpage\n\n')
            
            for i, chapter_file in enumerate(chapter_files):
                logger.info(f"Processing {chapter_file.name}...")
                
                with open(chapter_file, 'r', encoding='utf-8') as infile:
                    content = infile.read()
                
                # Add page break between chapters (except for first chapter)
                if i > 0:
                    outfile.write('\n\n\\newpage\n\n')
                
                outfile.write(content)
                outfile.write('\n\n')
        
        logger.info(f"Combined markdown created: {combined_file}")
        return combined_file

    def generate_epub(self, combined_file: Path, metadata: Optional[dict]) -> Path:
        """Generate EPUB ebook from combined markdown."""
        epub_file = self.output_dir / "regtech_guide.epub"
        
        logger.info("Generating EPUB...")
        
        if metadata:
            author = metadata.get("author", "Robert Betts")
            if isinstance(author, list):
                author = ", ".join(author)
        else:
            author = "Robert Betts"
        
        cmd = [
            'pandoc',
            str(combined_file),
            '-o', str(epub_file),
            '--epub-cover-image=cover.png' if (self.project_root / 'cover.png').exists() else '',
            '--toc',
            '--toc-depth=3',
            '--css=styles.css' if (self.project_root / 'styles.css').exists() else '',
            '--metadata', f'title={metadata.get("title", "Regtech Guide")}' if metadata else '',
            '--metadata', f'author={author}',
            '--metadata', f'date={metadata.get("date", "2025")}' if metadata else '',
            '--metadata', f'language={metadata.get("language", "en-GB")}' if metadata else '',
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

    def generate_pdf(self, combined_file: Path, metadata: Optional[dict]) -> Path:
        """Generate PDF from combined markdown."""
        pdf_file = self.output_dir / "regtech_guide.pdf"
        
        logger.info("Generating PDF...")
        
        if metadata:
            author = metadata.get("author", "Robert Betts")
            if isinstance(author, list):
                author = ", ".join(author)
        else:
            author = "Robert Betts"
            
        cmd = [
            'pandoc',
            str(combined_file),
            '-o', str(pdf_file),
            '--pdf-engine=mactex',
            '--toc',
            '--toc-depth=3',
            '--number-sections',
            '--highlight-style=tango',
            # '--geometry=margin=2.5cm',
            # '--fontsize=11pt',
            # '--documentclass=book',
            '--metadata', f'title={metadata.get("title", "Regtech Guide")}' if metadata else '',
            '--metadata', f'author={author}',
            '--metadata', f'date={metadata.get("date", "2025")}' if metadata else '',
            '--metadata', f'language={metadata.get("language", "en-GB")}' if metadata else '',
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

    def generate_html(self, combined_file: Path, metadata: Optional[dict]) -> Path:
        """Generate HTML version from combined markdown."""
        html_file = self.output_dir / "regtech_guide.html"
        
        logger.info("Generating HTML...")
        
        if metadata:
            author = metadata.get("author", "Robert Betts")
            if isinstance(author, list):
                author = ", ".join(author)
        else:
            author = "Robert Betts"
            
        cmd = [
            'pandoc',
            str(combined_file),
            '-o', str(html_file),
            '--standalone',
            '--toc',
            '--toc-depth=3',
            '--number-sections',
            '--css=styles.css' if (self.project_root / 'styles.css').exists() else '',
            '--metadata', f'title={metadata.get("title", "Regtech Guide")}' if metadata else '',
            '--metadata', f'author={author}',
            '--metadata', f'date={metadata.get("date", "2025")}' if metadata else '',
            '--metadata', f'language={metadata.get("language", "en-GB")}' if metadata else '',
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

    def generate_all(self) -> bool:
        """Generate all ebook formats."""
        logger.info("Starting ebook generation...")
        
        # Check dependencies
        if not self.check_dependencies():
            return False
        
        # Load metadata
        metadata = self.load_metadata()
        
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
        
        # Generate EPUB
        epub_file = self.generate_epub(combined_file, metadata)
        if not epub_file:
            success = False
        
        # Generate PDF
        pdf_file = self.generate_pdf(combined_file, metadata)
        if not pdf_file:
            success = False
        
        # Generate HTML
        html_file = self.generate_html(combined_file, metadata)
        if not html_file:
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
        success = generator.generate_all()
    else:
        # For individual formats, we'd need to implement specific methods
        logger.info(f"Individual format generation not yet implemented: {args.format}")
        success = generator.generate_all()
    
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
