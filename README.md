# RecipeGPT

A helpful recipe creator that uses ChatGPT to whip up delicious recipes for you!
Tell it what ingredients you have (typed, or from a photo) and it writes a recipe.

Built with Streamlit and the OpenAI API.

## Run it

```bash
pip install -r requirements.txt
streamlit run RecipeGPT.py
```

Needs an OpenAI key in `.streamlit/secrets.toml`:

```toml
OPENAI_API_KEY = "your key here"
```
