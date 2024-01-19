import spacy

# Load the spaCy English language model
nlp = spacy.load("en_core_web_sm")
def removeRepetitions(words):
    words = [word.lower() for word in words]
    words = list(set(words))
    return words
    
def extract_keywords(title, description):
    
    combined_text = f"{title}. {description}"
    # print("combined:", combined_text, type(combined_text))
    
    # Process the text using spaCy
    doc = nlp(combined_text)
    # print("doc:", doc, type(doc))
    # Extract keywords (non-stop words and nouns)
    for token in doc:
        if not token.is_stop:
            print(token, token.pos_)
    # print(doc.ents)
    tech_terms = [ent.text for ent in doc.ents if ent.label_ in ["TECHNICAL_TERM", "ORG"]]
    # print("tech_terms:", tech_terms)
    tech_terms = list(set(tech_terms))
    keywords = [token.text for token in doc if not token.is_stop and token.pos_ in ["NOUN", "PROPN"]]
    keywords = list(set(keywords))
    print("tech_terms:", tech_terms)
    print("keywords:", keywords)
    for tt in tech_terms:
        for kw in keywords:
            if kw in tt:
                keywords.remove(kw)
        keywords.append(tt)
    keywords = removeRepetitions(keywords)
    return keywords