# ChatGPT Sort v2 - prawdziwe API call do GPT-4o-mini
# Sortuje listę przez wysłanie jej do OpenAI API.
# Wymaga: pip install openai + zmiennej środowiskowej OPENAI_API_KEY
# Bez klucza uruchamia wersję mock.

import os
import json

try:
    from openai import OpenAI
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False

from data import *

def chatgpt_sort_api(lista):
    if not OPENAI_AVAILABLE:
        print("[ChatGPTSort]: pip install openai")
        return lista
    if not os.environ.get("OPENAI_API_KEY"):
        print("[ChatGPTSort]: Brak OPENAI_API_KEY")
        return lista
    lst = lista.copy()
    prompt = f"Sort this array ascending, return ONLY a JSON array.\nArray: {lst}\nResponse: [1, 2, 3, ...]"
    print(f"[ChatGPTSort]: Wysyłam do GPT: {lst}")
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0,
            max_tokens=500
        )
        answer = response.choices[0].message.content.strip()
        print(f"[ChatGPTSort]: GPT odpowiedział: {answer}")
        return json.loads(answer)
    except json.JSONDecodeError:
        print("[ChatGPTSort]: Halucynacja - nieparsowalna odpowiedź!")
        return lst
    except Exception as e:
        print(f"[ChatGPTSort]: Błąd API: {e}")
        return lst

def chatgpt_sort_mock(lista):
    import random, time
    lst = lista.copy()
    print(f"[ChatGPTSort MOCK]: Pytam GPT o {len(lst)} elementów...")
    time.sleep(0.3)
    if random.random() < 0.05:
        print("[ChatGPTSort MOCK]: 'As an AI language model, I cannot...'")
        return lst
    print("[ChatGPTSort MOCK]: Posortowane!")
    return sorted(lst)

if __name__ == "__main__":
    if OPENAI_AVAILABLE and os.environ.get("OPENAI_API_KEY"):
        print(chatgpt_sort_api(losowa))
    else:
        print(chatgpt_sort_mock(losowa))
        print("\nAby użyć API: pip install openai && $env:OPENAI_API_KEY='klucz'")
