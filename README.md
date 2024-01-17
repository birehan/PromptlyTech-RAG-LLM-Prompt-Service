# PromptlyTech RAG LLM Optimization

Welcome to the PromptlyTech repository dedicated to optimizing Language Models (LLMs) through advanced Prompt Engineering and the implementation of Retrieve, Answer, Generate (RAG) techniques. This toolkit focuses on streamlining prompt services for enhanced AI capabilities.

## Key Services
1. **Automatic Prompt Generation Service:**
   - Simplify the creation of effective prompts to harness the power of LLMs efficiently.

2. **Automatic Test Case Generation Service:**
   - Automate the generation of diverse test cases for comprehensive coverage and improved reliability.

3. **Prompt Testing and Ranking Service:**
   - Evaluate and rank prompts based on effectiveness, ensuring optimal outcomes from LLMs.

## Features
- Efficient prompt engineering for business contexts.
- Seamless integration with state-of-the-art LLMs like GPT-3.5 and GPT-4.
- Automated testing and ranking to enhance user engagement and satisfaction.

## Getting Started

1. Clone this repository:

```sh
git clone https://github.com/birehan/PromptlyTech-RAG-LLM-Prompt-Service.git
cd PromptlyTech-RAG-LLM-Prompt-Service
```

2. Setup environment variables on `.env`:

(create .env file in the [Title](Makefile)root directory)

```bash
#################
# Development env
#################

OPENAI_API_KEY=""
VECTORDB_MODEL="gpt-3.5-turbo"
```


# Installation

**Run**

```bash
# create virtual environment
python3 -m venv venv

# activate
source venv/bin/activate

# install requirements
pip install -r requirements.txt

# to generate test data
make data_generate

# to evaluate user input data (prob., accur., confid.)
make data_evaluate
```

## Contribution Guidelines
We welcome contributions from the community. Feel free to open issues, submit pull requests, and collaborate with us to improve the toolkit.

## License
This project is licensed under the [MIT License](LICENSE.md).

Let's optimize language models together! 🚀
