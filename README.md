# Regtech Guid

Generative AI guide for building technology platforms and systems in regulated environments.

This project make use the FintechForge Method and agentic generative AI to curate content for a reglatory technology guide following the FintechForge Method.

## Highlevel book description

This Regtech Guide will provide a comprehensive guidence covering all aspects of aquiring, building, deploying and running software in regulated environments. The target audience is accedemics, writers, regulators, enterprise archtitects, software engineers and other technology professionals that work with technology in regulated environments. 


## Agent Personas
- **moderator**: Curate, introduce, moderate, expand and summarise all topics.
- **positive_expert**: Present optimistic, supportive, and forward-thinking perspectives on regtech topics, while maintaining factual accuracy and substantiating all claims.
- **software_engineer**: Focused on software engineering stack, SDLC patterns and practice. Has extensive experience on building software applictions for used in regulated environments. 
- **architect**: Focused on process and regulated requirements, expert of all regulated aspects that govern use and implementation of technology in regulated environments. 
- **sre**: Focussed monitoring, observability, change management, deployment and resiliance of regulated technology 
- **negative_expert**: Present critical, skeptical, and opposing views on Regtech topics, while maintaining factual accuracy and substantiating all claims. Not simply negative for the sake of being negative, but providing constructive criticism and highlight genuine areas of concern.

## General Contribution Guidelines

All facts presented must always be substantiated by publicly available content and or code. tracking the reference sources is very important. The medium of communication will be UK English or the Python programming language as appropriate.

## FintechForge Method

A document topics.md, will contain a list of relevant discussion topics. Each topic will be tracked as completed, in_discussion and future_topic.

Each of the agents will read from the topics.md file and contribute to the discussion until the topic is marked as complete. The discussion will take place in a new file named appropriately for the topic. Each agent's contributions on the topic will be recorded here. The contributing agents will end their individual contribution to the topic with the phrase agent xxx complete.

When all the contributing agents have completed, the moderator will summarize the discussion. In topics.md, the in_progress topic will be updated to completed and the status of the next topic will be updated to in_discussion, and a new file for the next topic created. The contributing agents will then to be prompted to initiate their contribution to the discussion on the in_progress topic.

