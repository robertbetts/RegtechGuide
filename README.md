# Regtech Guide

A reference guide for building technology platforms and systems in regulated environments. The content was curated using the FintechForge Method.

## Description

This Regtech Guide provides a comprehensive reference guide covering all aspects of aquiring, building, deploying and running software in regulated environments. The target audience are accedemics, writers, regulators, enterprise archtitects, software engineers and other technology professionals who work with technology in regulated environments. 

## Method Prespectives - Agent Personas
- **moderator**: Curate, introduce, moderate, expand and synthesize.
- **positive_expert**: Present optimistic, supportive, and forward-thinking perspectives on regtech topics, while maintaining factual accuracy and substantiating all claims.
- **software_engineer**: Focused on software engineering: technology stack, SDLC patterns and practice. Has extensive experience on building software applictions in regulated environments. 
- **architect**: Focused on process, specific regulatory requirements. Expert of all regulated aspects that govern the use, implementation and scaling of technology in regulated environments.  
- **sre**: Focussed on monitoring, observability, change management, deployment and resiliance of regulated technology. 
- **negative_expert**: Present critical, skeptical, and opposing views on regtech topics, while maintaining factual accuracy and substantiating all claims. Not simply negative for the sake of being negative, but providing constructive criticism and highlighting genuine areas of concern.

## General Contribution Guidelines

All facts presented must always be substantiated by publicly available content and or code. - Recording reference sources of fact is required. 
- The medium of communication will be UK English or the Python programming language as appropriate.

## FintechForge Method

Generate and review the file topics.md. 
- This file will contain a list of relevant discussion topics. 
- Each topic will be tracked with the the statuses of completed, in_discussion or future_topic.
- All method perspectives will contribute to all topics.

### Discussion and Research Orchestration

Each of the perspective agents will read from the topics.md file and contribute to the discussion until the topic is marked as complete. 
- Each topic discussion is recorded in a file named appropriately for the topic. 
- Each agent's contribution on the topic will be recorded in this discussion topic file.
- Each agents will end their contribution with the phrase agent xxx complete.
- It is allowed that each agent could make multiple contributions, each seperately recorded.

When all the contributing agents are complete, the moderator will synthesize the discussion and add this summary to the discussion topic file.
- In topics.md, the in_progress topic will be updated to completed.
- The status of the next topic will be updated to in_discussion
- A new discussion topic file for the next topic created. 
- The contributing agents will then to be prompted to initiate their contributions to the in_progress topic.

### Synthesizing and Production of the Final Reference Documentation

After all the discussion topics are complete, the moderator will synthesize each discussion topic into a single chapter. 
- Do not to overly duplicate topics across chapters, with a preference to referencing a topic in another chapter.
- Produce a book title / overview page for the Regtech Guide using the publishing metadata provided in the file metadata.yaml.
- Produce a single file with structured with the overview, contents page and then each of the synthesized chapters.
    - Render versions in markdown, HTML, epub and pdf formats 
