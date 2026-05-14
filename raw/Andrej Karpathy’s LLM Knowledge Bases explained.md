---
title: "Andrej Karpathy’s LLM Knowledge Bases explained"
source: "https://medium.com/data-science-in-your-pocket/andrej-karpathys-llm-knowledge-bases-explained-2d9fd3435707"
author:
  - "[[Mehul Gupta]]"
published: 2026-04-12
created: 2026-04-15
description: "Andrej Karpathy’s LLM Knowledge Bases explained What is LLM Knowledge Bases by Andrej Karpathy? If you follow the world of Artificial Intelligence, you have likely heard of Andrej Karpathy. He is …"
tags:
  - "clippings"
---
## What is LLM Knowledge Bases by Andrej Karpathy?

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*vKSqZxOBavfBvWP8)

Photo by detait on Unsplash

If you follow the world of Artificial Intelligence, you have likely heard of Andrej Karpathy. He is one of the founding researchers at OpenAI and formerly the Director of AI at Tesla. In simple terms, he is one of the smartest people in the field.

Recently, Karpathy shared a fascinating change in how he works. He used to spend most of his time writing computer code. Now, he spends his time using AI to build a personal “knowledge base.”

![](https://miro.medium.com/v2/resize:fit:1280/format:webp/0*2by3vkFpAUgnFmiH)

> Think of a knowledge base as a super-powered, digital encyclopedia that is built just for you. It holds everything you know about a specific topic, organized perfectly.

In this blog post, we are going to break down exactly how Karpathy builds these systems using simple tools and AI. You don’t need to be a computer genius to understand the concept.

## The Big Idea: From Coding to “Knowledge Work”

***Karpathy noticed that the newest AI models (like GPT-4 or Claude) are incredibly good at understanding and organizing text. So, instead of asking the AI to write software code, he started asking it to organize his research.***

> His goal was to create a system where he could dump raw information, like research papers, articles, and images, and have the AI turn it into a neat, organized library of knowledge that he can search and ask questions about later.

Here is the step-by-step breakdown of his system.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*8iSVQbNeqVf8d9cbjI5fkg.png)

## Step 1: Data Ingest (The “Raw” Folder)

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*Q0s_qZFswp4Uf_93M8SKrQ.png)

Everything starts with a folder on his computer called `raw`. This is the digital equivalent of a messy pile of documents on your desk.

### Karpathy fills this folder with anything he is interested in:

> **Articles:** Essays or blog posts from the web.
> 
> **Papers:** Academic research PDFs.
> 
> **Code:** Software repositories.
> 
> **Datasets:** Spreadsheets or numbers.
> 
> **Images:** Diagrams or charts.
> 
> **The Tooling:** To make this easy, he uses a browser extension called Obsidian Web Clipper. When he finds an interesting article online, he clicks a button, and it saves the article as a file on his computer.

Crucially, he also makes sure to download any images from those articles to his computer. Why? Because he wants the AI to be able to “see” the diagrams and charts, not just read the text.

## Step 2: The AI “Compiler” (Making the Wiki)

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*Bhf1NFL5FSyDkRH8r5gFsg.png)

Once the data is in the `raw` folder, the magic happens. Karpathy uses an LLM to act as a compiler.

> In computing, a “compiler” usually takes raw code and turns it into a working program. In this case, the AI takes the messy raw files and “compiles” them into a Wiki.

A Wiki is just a collection of text files (ending in.md) that link to each other, like Wikipedia. The AI does the heavy lifting:

> **Summarizing:** It reads every long paper and writes a short summary.
> 
> **Categorizing:** It groups similar topics together.
> 
> **Linking:** It creates “backlinks,” so if Article A mentions Article B, they are linked together.
> 
> **Writing Articles:** It actually writes new articles explaining specific concepts found in the data.

Karpathy doesn’t write these summaries himself. The AI does it all.

## Step 3: The IDE (The Command Center)

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*DznVV_wqCRRzO5mhqxjkEQ.png)

To view all this information, Karpathy uses a free note-taking app called Obsidian. Think of Obsidian as his dashboard or “IDE” (Integrated Development Environment). In this setup, Obsidian is where he can see:

- The original raw data.
- The shiny new Wiki the AI created.
- Visualizations of the data.

> The Golden Rule: Karpathy rarely touches the Wiki files himself. He treats the Wiki as “AI territory.” The AI writes it, updates it, and maintains it. Karpathy just reads it.

## Step 4: Q&A (Asking the Hard Questions)

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*7ctibH0gSDZrwlBWJQKaRw.png)

This is where the system becomes really useful.

> Karpathy’s current research Wiki is quite large, about 100 articles and roughly 400,000 words. That is roughly the length of 4 to 5 full-length novels!

Because the AI helped build this Wiki, it knows the information inside and out. Karpathy can ask it complex questions like, “What are the connections between Concept A and Concept B?” or “Summarize the main arguments from these five specific papers.”**Why no fancy search tools?** *Usually, when people build big AI systems, they use something called RAG (Retrieval-Augmented Generation). This is a complex technique to help the AI find the right file.*

However, Karpathy found that he doesn’t need complex tools yet. Because his Wiki is well-organized by the AI (with good summaries and an index), the AI can simply read the relevant summaries and find the answer on its own. It’s simple and effective.

## Step 5: Output (More Than Just Text)

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*jPKvHYt_MI3PkHHHhrt1zg.png)

When you ask an AI a question, it usually just spits out text in a chat window. Karpathy likes to do things differently. He asks the AI to give him files as output:

> **Markdown Files:** A new note for his Wiki.
> 
> **Slide Shows:** Using a tool called Marp, the AI can turn research into a presentation deck.
> 
> **Charts/Graphs:** The AI can write code to create graphs using a tool called Matplotlib.

He views all these outputs directly inside Obsidian. Best of all, he often takes these new files and puts them *back* into his Wiki. This means every time he asks a question, his knowledge base grows bigger and smarter.

## Step 6: Linting (The Cleanup Crew)

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*_r11PKNEZeOKYLdG2lJCQg.png)

***Just like a computer programmer checks their code for errors, Karpathy runs “health checks” on his Wiki.*** He asks the AI to:

> Find inconsistent data (where one file contradicts another).
> 
> Fill in missing information (sometimes even using web search to find gaps).
> 
> Find interesting connections that might lead to new research topics.

This acts like a cleanup crew, constantly tidying up the library and suggesting new books to read.

## Step 7: Extra Tools

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*fxlTiEN6nhrpujRbR1Tdhg.png)

Karpathy admits that he writes a few small custom scripts (mini-programs) to help the AI. For example, he wrote a very simple search engine for his Wiki.

He can use this search engine himself, but more often, he lets the AI use it. The AI can run the search engine via a command line to find specific data it needs to answer a tough question.

## The Future: Training the AI

Right now, the AI “reads” the Wiki to answer questions. It uses its short-term memory (context window) to look at the files. Karpathy’s next goal is to use Fine-Tuning.

**Fine-tuning is like permanently teaching the AI**. Instead of showing the AI the files every time he asks a question, he wants to train the AI so that the knowledge is baked into its “brain.” This would make the AI an expert on his research topics without needing to look at the notes anymore.

## Summary (The TL;DR)

Andrej Karpathy has moved away from just writing code to building “Knowledge Bases.” Here is the simple workflow:

> **Collect:** Save raw articles, papers, and images into a folder.
> 
> **Compile:** Use an LLM to read the raw data and turn it into an organized, summarized Wiki (linked text files).
> 
> **View:** Use Obsidian to read and view the Wiki.
> 
> **Ask:** Ask the AI complex questions about the Wiki. The AI reads its own summaries to find answers.
> 
> **Create:** Have the AI output slide shows, charts, or new notes, which are then added back to the Wiki.
> 
> **Maintain:** Let the AI fix errors and fill in gaps.

Karpathy points out that right now, this is a “hacky” collection of scripts. But he believes there is a huge opportunity here for someone to build a polished product that makes this easy for everyone.

It’s a glimpse into a future where we don’t just manage files; we manage knowledge with the help of an AI partner.