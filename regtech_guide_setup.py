#!/usr/bin/env python3
"""
Regtech Guide Setup

This script sets up the regtech guide project by creating the necessary folders and files.
"""

import os
import re
from typing import Dict, List, Optional
import logging
import sys
import subprocess
from collections import OrderedDict
from pathlib import Path
import time


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(lineno)-4d %(message)s',
    handlers=[
        logging.FileHandler('prompt_generator.log'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)


class RegtechGuideSetup:
    def __init__(self, project_root: str = ".", simulation: bool = False):
        self.project_root = Path(project_root)
        self.simulation = simulation
        self.personas_folder = self.project_root / 'personas'
        self.discussions_folder = self.project_root / 'discussions'
        self.topics_file = self.discussions_folder / 'topics.md'
        self.book_folder = self.project_root / 'book'
        self.licence_file = self.book_folder / 'LICENCE'
        self.metadata_file = self.book_folder / 'metadata.yaml'


    def generate_prompt(self) -> str:
        prompt = f""" 
Using @README.md as a guide:
- in the personas folder create the agent personas that will drive their respective characteristics, behaviours and contributions
- in the discussions folder create the topics.md file that will drive all the subject matter discussions and eventually be synthesized into chapters for the final book.
    - Each topic will be tracked with the statuses of completed, in_discussion or future_topic.
    - All method perspectives will contribute to all topics.
- in the book folder initiate an ebook publishing metadata.yaml if it does not exist, default to the creative commons license
- in the book folder initiate a LICENCE file if it does not exist, default to the creative commons license

"""
        return prompt

    def run_cursor_agent(self, agent_prompt: str, simulation: bool = False) -> bool:
        """Run cursor-agent with the specified parameters."""

        cmd = [
            'cursor-agent',
            '-p', 
            agent_prompt
        ]
        # logger.debug(f"Command: {' '.join(cmd)}")
        
        try:
            # Run cursor-agent
            if simulation:
                logger.info(f"Simulation mode: {agent_prompt}")
                return True
            else:
                logger.info(f"Running cursor-agent")
                result = subprocess.run(cmd, capture_output=False, text=True, timeout=300)  # 5 minute timeout
            
                if result.returncode == 0:
                    logger.info(f"prompt completed successfully")
                    return True
                else:
                    logger.error(f"prompt failed with return code {result.returncode}")
                    logger.error(f"Error output: {result.stderr}")
                    return False
                
        except subprocess.TimeoutExpired:
            logger.error(f"Prompt timed out after 5 minutes")
            return False
        except Exception as e:
            logger.error(f"Error running prompt: {e}")
            return False    

    def setup(self):
        self.book_folder.mkdir(parents=True, exist_ok=True)
        self.personas_folder.mkdir(parents=True, exist_ok=True)
        self.discussions_folder.mkdir(parents=True, exist_ok=True)
        agent_prompt = self.generate_prompt()
        self.run_cursor_agent(agent_prompt, self.simulation)


def main():
    """Command-line interface for the regtech guide setup."""
    import sys
    generator = RegtechGuideSetup()
    generator.setup()
    return
    

if __name__ == "__main__":
    main()
