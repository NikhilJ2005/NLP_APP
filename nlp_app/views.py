

from django.shortcuts import render
import spacy

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

def index(request):
	if request.method == "POST":
		text = request.POST.get("text")
		doc = nlp(text)
		entities = [(ent.text, ent.label_) for ent in doc.ents]
		return render(request, "index.html", {"entities": entities, "text": text})
	return render(request, "index.html")