from django.shortcuts import render
import openai
from dotenv import load_dotenv
import os
#python manage.py runserver

def home(request):
    return render(request, 'pages/home.html')

def essay_writing(request):
    if request.method == 'POST':
        prompt = request.POST['question']
        language = request.POST['language']
        prompt = "Write an essay in "+language+" about "+prompt
        print(prompt)
        load_dotenv()
        openai.api_key = os.environ.get("GPT3_KEY")
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=prompt,
            max_tokens=200,
        )
        answer = response['choices'][0]['text']
        print(answer)
    else:
        answer = None
    return render(request, 'pages/essay_writing.html', {'answer': answer})

def paraphrase(request):
    if request.method == 'POST':
        prompt = request.POST['question']
        language = request.POST['language']
        prompt = "Paraphrase in "+language+" this "+prompt
        print(prompt)
        load_dotenv()
        openai.api_key = os.environ.get("GPT3_KEY")
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=prompt,
            max_tokens=200,
        )
        answer = response['choices'][0]['text']
        print(answer)
    else:
        answer = None
    return render(request, 'pages/paraphrase.html', {'answer': answer})

def about(request):
    return render(request, 'pages/about.html')
