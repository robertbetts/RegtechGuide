# Prompt Template Usage Guide

This guide explains how to use the prompt templates and generator for agent contributions to the Regtech Guide.

## Files Overview

- **`agent_prompt_template.md`**: Static template with placeholders for manual customization
- **`prompt_generator.py`**: Python script that automatically generates prompts with context
- **`PROMPT_USAGE.md`**: This usage guide

## Method 1: Using the Python Generator (Recommended)

The `prompt_generator.py` script automatically reads context files and generates complete prompts.

### Basic Usage

```bash
python prompt_generator.py <agent_name> <topic_title>
```

### Examples

```bash
# Generate prompt for software engineer on software engineering topic
python prompt_generator.py software_engineer "Software Engineering for Regulated Environments"

# Generate prompt for moderator on introduction topic
python prompt_generator.py moderator "Introduction to Regulatory Technology"

# Generate prompt for positive expert on business case topic
python prompt_generator.py positive_expert "The Business Case for Regtech"
```

### Available Agents

- `moderator`
- `positive_expert`
- `software_engineer`
- `functional_architect`
- `sre`
- `negative_expert`

### Available Topics

Run without arguments to see all available topics:

```bash
python prompt_generator.py
```

## Method 2: Manual Template Customization

Use the `agent_prompt_template.md` file and manually replace placeholders:

### Placeholders to Replace

- `[AGENT_NAME]`: The specific agent name
- `[AGENT_PERSONA_FILE]`: The corresponding persona file
- `[TOPIC_TITLE]`: The specific topic title
- `[TOPIC_DESCRIPTION]`: The topic description
- `[LIST_OF_AGENTS]`: The contributing agents for this topic
- `[TOPIC_STATUS]`: Current status
- `[TOPIC_DISCUSSION_FILE]`: The discussion file name

### Example Manual Customization

```markdown
You are the software_engineer agent contributing to the Regtech Guide project. Your role is to provide expert perspective on the topic "Software Engineering for Regulated Environments" following your specific persona characteristics and expertise.

## Context Files
Please review these essential context files before contributing:

### Project Overview
- README.md: Project description, methodology, and contribution guidelines
- topics.md: Complete list of topics and discussion process
- software_engineer.md: Your specific persona characteristics and behavioral guidelines

### Current Topic Context
- 04_software_engineering_for_regulated_environments.md: Current discussion file for this topic (if exists)
- Previous agent contributions (if any)

[... continue with customized content]
```

## What the Generated Prompt Includes

### Context Files
- **README.md**: Project overview and methodology
- **topics.md**: Complete topic list and discussion process
- **Agent persona file**: Specific characteristics and guidelines
- **Topic discussion file**: Current discussion (if exists)

### Agent-Specific Content
- **Core Characteristics**: Extracted from persona file
- **Contribution Style**: How the agent should contribute
- **Knowledge Areas**: Relevant expertise areas
- **Quality Standards**: Requirements for contributions

### Topic-Specific Content
- **Topic Description**: From topics.md
- **Contributing Agents**: List of agents for this topic
- **Current Status**: Topic status (future_topic, in_discussion, completed)

### Contribution Guidelines
- **Requirements**: What the agent must do
- **Format**: Expected output structure
- **Quality Checklist**: Items to verify before submission
- **Integration**: How to work with other agents

## Workflow Integration

### For New Topics

1. **Select Topic**: Choose next topic from topics.md
2. **Update Status**: Change status to "in_discussion" in topics.md
3. **Create Discussion File**: Create topic discussion file
4. **Generate Prompts**: Use generator for each contributing agent
5. **Agent Contributions**: Each agent contributes using their prompt
6. **Moderation**: Moderator synthesizes and marks complete

### For Existing Topics

1. **Check Discussion File**: Review existing contributions
2. **Generate Prompt**: Use generator for next contributing agent
3. **Agent Contribution**: Agent contributes building on existing work
4. **Continue Process**: Until all agents have contributed

## Quality Assurance

### Before Using Prompts

- [ ] Verify all context files exist and are up-to-date
- [ ] Check topic status in topics.md
- [ ] Ensure agent persona files are current
- [ ] Review any existing contributions

### After Agent Contributions

- [ ] Verify contribution follows expected format
- [ ] Check that agent ended with "agent [name] complete"
- [ ] Ensure all claims are substantiated
- [ ] Confirm UK English usage throughout

## Troubleshooting

### Common Issues

1. **File Not Found**: Ensure all context files exist in project root
2. **Topic Not Found**: Check topic title spelling in topics.md
3. **Agent Not Found**: Verify agent name matches available agents
4. **Encoding Issues**: Ensure files are UTF-8 encoded

### Error Messages

- `Unknown agent`: Check agent name against available agents
- `Topic description not found`: Verify topic title in topics.md
- `File not found`: Check file paths and existence

## Best Practices

1. **Always Use Generator**: Prefer automated generation over manual customization
2. **Review Context**: Ensure all context files are current before generating prompts
3. **Validate Output**: Check generated prompts for completeness
4. **Maintain Consistency**: Use same prompt structure for all agents
5. **Track Progress**: Update topic status as discussions progress

## Integration with FintechForge Method

The prompt system supports the FintechForge Method by:

- **Ensuring Consistency**: All agents follow same structure
- **Providing Context**: Complete context for informed contributions
- **Maintaining Quality**: Built-in quality standards and checklists
- **Supporting Collaboration**: Clear integration guidelines
- **Facilitating Progress**: Status tracking and process management
