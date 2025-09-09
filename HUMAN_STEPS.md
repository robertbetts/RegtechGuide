## Step 1 - run regtech_guide_setup.py


## Step 2 - Human Review

- Review the topics.md and agent personal files
- Determine the appropriate license and create the publishing metadata.yaml file

## Step 3 - run discussion_generator.py

## Step 4 - run book_generator.py

## Step 5 - prompt

Create book/Book_Overview.md
- Using discussions/topics.md as a guide and all the book/Chapter_*.md files
- Create an introduction section that briefly summarises each each chapter
- Get book license info from README.md

## Step 6 - prompt (Optional step for additional analysis of the generative content)

Review all the files in the folder book, referencing Overview.md structural guides. Map in detail all the themes in the book, connecting and highlighting duplicated topics. 
- store all analysis output in an analysis folder
- create a table of theme, chapter, line numbers
- create a mermaid flow to visually represent these relationships

## Step 8 - run ebook_generator.py
