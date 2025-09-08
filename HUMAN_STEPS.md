## Step 1 - run prompt

Using @README.md as a guide, create the agent personas that will drive their respective characteristics, behaviours and contributions. then create the topics.md file that will eventually be synthesized into chapters for the final book.
- initiate an ebook publishing metadata.yaml in a book folder if it does not exist
- initiate a LICENCE file in the book folder if it does not exist

## Step 2 - Human Review

- Review the topics.md and agent personal files
- Determine the appropriate license and create the publishing metadata.yaml file

## Step 3 - create prompt 

Create a prompt template which will used to initiate the context for each contributing persona to begin their contribution
- Include in the context references to README.md, topics.md and AGENT_PERSONA.md and discussion topic file to be added to.
- The agentic context must be reset for each contribution in order to provide consistent and repeatable contributions that fall within token memory limits.

## Step 4 - run prompt_generator.py

## Step 5 - run book_generator.py

## Step 6 - prompt

Using fintech_topics.md as a guide, create the book overview and contents page.
- Acknowledge the authors Robert Betts and Prof. A.I. Forge
- Reference the creative commons license from the file LICENSE.
- Place the overview_and_contents.md file in the book folder. hyperlink each chapter to the respective chapter file in the book folder.

## Step 7 - prompt (Optional step for additional analysis of the generative content)

Review all the files in ./book, referencing overview_and_contents.md as a structural guide. Map out in detail all the themes in the book, connecting and highlighting duplicate topics. 
- store all analysis output in an analysis folder
- create a table of theme, chapter, line numbers
- create a mermaid flow to visually represent these relationships

## Step 8 - run ebook_generator.py
