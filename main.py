from openai import OpenAI
client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

from duckduckgo_search import DDGS
def search_duckduckgo(query, max_results=5):
    results = []
    with DDGS() as ddgs:
        for r in ddgs.text(query, max_results=max_results):
            results.append({
                'title': r['title'],
                'link': r['href'],
                'snippet': r['body']
            })
    return results

def agent(user_input):
    search_results = search_duckduckgo(user_input, max_results=3)
    context = "\n".join([f"Title: {res['title']}\nLink: {res['link']}\nSnippet: {res['snippet']}\n" for res in search_results])
    
    prompt = f"""You are an AI assistant. Use the following search results to answer the user's question.