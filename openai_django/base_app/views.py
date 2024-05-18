from django.shortcuts import render
from django.http import JsonResponse
from .oai_queries import get_completion

def query_view(request):
    if request.method == 'POST':
        prompt = request.POST.get('prompt')
        response = get_completion(prompt)
        completion_text = response['choices'][0]['message']['content']
        return JsonResponse({'response': completion_text})
    return render(request, 'query.html')
