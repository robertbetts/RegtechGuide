#!/usr/bin/env python3
"""
Prompt Generator for Regtech Guide Agent Contributions

This script generates customized prompts for each agent persona when contributing to topics.
It reads the necessary context files and creates a complete prompt with all required information.
"""

import os
import re
from typing import Dict, List, Optional

class PromptGenerator:
    def __init__(self, project_root: str = "."):
        self.project_root = project_root
        self.discussion_folder = 'discussion'
        self.context_files = {
            'README.md': 'Project description, methodology, and contribution guidelines',
            'topics.md': 'Complete list of topics and discussion process',
        }
        
        self.agent_personas = {
            'moderator': 'moderator.md',
            'positive_expert': 'positive_expert.md',
            'software_engineer': 'software_engineer.md',
            'functional_architect': 'functional_architect.md',
            'sre': 'sre.md',
            'negative_expert': 'negative_expert.md'
        }

    def read_file(self, filepath: str) -> str:
        """Read a file and return its contents."""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            return f"File not found: {filepath}"

    def extract_topic_info(self, topic_title: str) -> Dict[str, str]:
        """Extract topic information from topics.md."""
        topics_content = self.read_file(os.path.join(self.project_root, 'topics.md'))
        
        # Find the topic section
        topic_pattern = rf"### \d+\. {re.escape(topic_title)}"
        topic_match = re.search(topic_pattern, topics_content)
        
        if not topic_match:
            return {
                'description': 'Topic description not found',
                'contributing_agents': 'Contributing agents not found',
                'status': 'future_topic'
            }
        
        # Extract the topic section
        topic_section_start = topic_match.start()
        next_topic_pattern = r"### \d+\."
        next_topic_match = re.search(next_topic_pattern, topics_content[topic_section_start + 1:])
        
        if next_topic_match:
            topic_section = topics_content[topic_section_start:topic_section_start + next_topic_match.start() + 1]
        else:
            topic_section = topics_content[topic_section_start:]
        
        # Extract information
        description_match = re.search(r'\*\*Description\*\*: (.+)', topic_section)
        agents_match = re.search(r'\*\*Contributing Agents\*\*: (.+)', topic_section)
        status_match = re.search(r'\*\*Status\*\*: (.+)', topic_section)
        
        return {
            'description': description_match.group(1) if description_match else 'Description not found',
            'contributing_agents': agents_match.group(1) if agents_match else 'Contributing agents not found',
            'status': status_match.group(1) if status_match else 'future_topic'
        }

    def extract_persona_characteristics(self, agent_name: str) -> Dict[str, str]:
        """Extract key characteristics from agent persona file."""
        persona_file = self.agent_personas.get(agent_name)
        if not persona_file:
            return {}
        
        persona_content = self.read_file(os.path.join(self.project_root, persona_file))
        
        # Extract key sections
        characteristics = {}
        
        # Core Characteristics
        core_match = re.search(r'## Core Characteristics\n(.*?)(?=\n## |$)', persona_content, re.DOTALL)
        if core_match:
            characteristics['core_characteristics'] = core_match.group(1).strip()
        
        # Contribution Style
        style_match = re.search(r'## Contribution Style\n(.*?)(?=\n## |$)', persona_content, re.DOTALL)
        if style_match:
            characteristics['contribution_style'] = style_match.group(1).strip()
        
        # Knowledge Areas
        knowledge_match = re.search(r'## Knowledge Areas\n(.*?)(?=\n## |$)', persona_content, re.DOTALL)
        if knowledge_match:
            characteristics['knowledge_areas'] = knowledge_match.group(1).strip()
        
        # Quality Standards
        quality_match = re.search(r'## Quality Standards\n(.*?)(?=\n## |$)', persona_content, re.DOTALL)
        if quality_match:
            characteristics['quality_standards'] = quality_match.group(1).strip()
        
        return characteristics

    def generate_prompt(self, agent_name: str, topic_title: str) -> str:
        """Generate a complete prompt for the specified agent and topic."""
        
        # Validate agent name
        if agent_name not in self.agent_personas:
            raise ValueError(f"Unknown agent: {agent_name}. Available agents: {list(self.agent_personas.keys())}")
        
        # Get topic information
        topic_info = self.extract_topic_info(topic_title)
        
        # Get persona characteristics
        persona_chars = self.extract_persona_characteristics(agent_name)
        
        # Generate discussion file name
        topic_number = self.get_topic_number(topic_title)
        discussion_file = f"{self.discussion_folder}/{topic_number:02d}_{topic_title.lower().replace(' ', '_').replace('&', 'and')}.md"
        
        # Build the prompt
        prompt = f"""You are the {agent_name} agent contributing to the Regtech Guide project. Your role is to provide expert perspective on the topic "{topic_title}" following your specific persona characteristics and expertise.

## Context Files
Please review these essential context files before contributing:

### Project Overview
- README.md: Project description, methodology, and contribution guidelines
- topics.md: Complete list of topics and discussion process
- {self.agent_personas[agent_name]}: Your specific persona characteristics and behavioral guidelines

### Current Topic Context
- {discussion_file}: Current discussion file for this topic (if exists)
- Previous agent contributions (if any)

## Your Role as {agent_name}

Based on your persona file ({self.agent_personas[agent_name]}), you should:

### Core Characteristics
{persona_chars.get('core_characteristics', 'Core characteristics not found')}

### Contribution Style
{persona_chars.get('contribution_style', 'Contribution style not found')}

### Knowledge Areas
{persona_chars.get('knowledge_areas', 'Knowledge areas not found')}

### Quality Standards
{persona_chars.get('quality_standards', 'Quality standards not found')}

## Topic: {topic_title}

**Topic Description**: {topic_info['description']}

**Contributing Agents**: {topic_info['contributing_agents']}

**Current Status**: {topic_info['status']}

## Your Contribution Requirements

1. **Read and Understand**: Review all context files, especially your persona file and any existing contributions
2. **Provide Expert Perspective**: Contribute from your specific expertise area and persona characteristics
3. **Substantiate Claims**: All facts must be substantiated by publicly available content or code
4. **Use UK English**: Maintain UK English throughout your contribution
5. **End Appropriately**: Conclude your contribution with "agent {agent_name} complete"

## Contribution Guidelines

- **Length**: Provide comprehensive but focused contributions (typically 500-1500 words)
- **Structure**: Use clear headings and structure for readability
- **Evidence**: Include specific examples, case studies, or code references where appropriate
- **Balance**: Maintain your persona perspective while being constructive and factual
- **Integration**: Consider how your contribution fits with other agent perspectives

## Expected Output Format

```markdown
# {agent_name} Contribution to {topic_title}

## Key Points
[Bullet points of main contributions]

## Detailed Analysis
[Comprehensive analysis from your perspective]

## Specific Recommendations
[Actionable recommendations based on your expertise]

## Examples and Evidence
[Specific examples, case studies, or code references]

## Considerations and Implications
[Important considerations from your perspective]

## Conclusion
[Summary of your contribution and key takeaways]

agent {agent_name} complete
```

## Quality Checklist

Before submitting your contribution, ensure:
- [ ] All claims are substantiated with evidence
- [ ] Contribution aligns with your persona characteristics
- [ ] UK English is used throughout
- [ ] Contribution is comprehensive and well-structured
- [ ] Specific examples and recommendations are provided
- [ ] Contribution ends with "agent {agent_name} complete"

## Additional Context

If this is the first contribution to this topic, you are setting the foundation for discussion. If other agents have already contributed, build upon their insights while maintaining your unique perspective.

Remember: Your role is to provide expert insight from your specific area of expertise while maintaining the collaborative spirit of the FintechForge Method.
"""
        
        return prompt

    def get_topic_number(self, topic_title: str) -> int:
        """Extract topic number from topics.md."""
        topics_content = self.read_file(os.path.join(self.project_root, 'topics.md'))
        
        # Find the topic number
        topic_pattern = rf"### (\d+)\. {re.escape(topic_title)}"
        match = re.search(topic_pattern, topics_content)
        
        if match:
            return int(match.group(1))
        else:
            return 0

    def list_available_agents(self) -> List[str]:
        """Return list of available agent names."""
        return list(self.agent_personas.keys())

    def list_available_topics(self) -> List[str]:
        """Return list of available topics from topics.md."""
        topics_content = self.read_file(os.path.join(self.project_root, 'topics.md'))
        
        # Find all topic titles
        topic_pattern = r"### \d+\. (.+)"
        matches = re.findall(topic_pattern, topics_content)
        
        return matches

def main():
    """Command-line interface for the prompt generator."""
    import sys
    
    generator = PromptGenerator()
    
    if len(sys.argv) < 3:
        print("Usage: python prompt_generator.py <agent_name> <topic_title>")
        print(f"Available agents: {', '.join(generator.list_available_agents())}")
        print(f"Available topics: {', '.join(generator.list_available_topics())}")
        return
    
    agent_name = sys.argv[1]
    topic_title = sys.argv[2]
    
    try:
        prompt = generator.generate_prompt(agent_name, topic_title)
        print(prompt)
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
