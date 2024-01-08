# ChatGPT vs LLaMA: Impact, Reliability, and Challenges in Stack Overflow Discussions

## Overview

This repository contains the code and supplementary material associated with the research paper titled **ChatGPT vs LLaMA: Impact, Reliability, and Challenges in Stack Overflow Discussions**. The paper explores the impact on the usage of Stack Overflow after the release of ChatGPT. Furthermore, it also investigates the potential of LLMs, ChatGPT and LLaMa, to support users in answering SO questions and the main challenges that current LLMs face.

## Table of Contents

- [Research Paper Title](#research-paper-title)
    - [Overview](#overview)
    - [Table of Contents](#table-of-contents)
    - [Paper Abstract](#paper-abstract)
    - [Code Structure](#code-structure)
    - [Getting Started](#getting-started)
    - [Usage](#usage)

## Paper Abstract

Since its release in November 2022, ChatGPT has shaken up Stack Overflow, the premier platform for developers’ queries on programming and software development. Demonstrating an ability to generate instant, human-like responses to technical questions, ChatGPT has ignited debates within the developer community about the evolving role of human-driven platforms in the age of generative AI. Two months after ChatGPT’s release, Meta released its answer with its own Large Language Model (LLM) called LLaMA: the race was on. We conducted an empirical study analyzing questions from Stack Overflow and using these LLMs to address them. This way, we aim to ① measure user engagement evolution with Stack Overflow over time; ② quantify the reliability of LLMs’ answers and their potential to replace Stack Overflow in the long term; ③ identify and understand why LLMs fails; and ④ compare LLMs together. Our empirical results are unequivocal: ChatGPT and LLaMA challenge human expertise, yet do not outperform it for some domains, while a significant decline in user posting activity has been observed. Furthermore, we also discuss the impact of our findings regarding the usage and development of new LLMs

## Code Structure

├── data/ # Sample or required data

├── src/ # Source code

│ ├── analysis/ # Code for generating main analysis

│ ├── input/ # Code for handling with sample selection

│ ├── llm/ # Code for support when prompting llms

│ ├── output_generation/ # Code for generating output files

│ ├── post_analysis/ # Code for generating charts

│ ├── r-analysis/ # Code for generating R analysis

│ ├── similarity-analysis/ # Code for prompting LLMs

│ ├── stack/ # Utility code

├── LICENSE # License file

├── README.md # Project README file

└── requirements.txt # Dependencies and requirements

## Getting Started

``git clone https://github.com/leusonmario/chat-stack.git``

``cd chat-stack``

``pip install -r requirements.txt``

## Usage

To run the main analysis, provide the required information on the ``__main__.py`` file.
After that, run the command ``python src/__main__.py``

As a result, different folders with the generated results will be available in the directory provided as input.
