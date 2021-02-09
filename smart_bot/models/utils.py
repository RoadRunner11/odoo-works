import spacy

nlp = spacy.load("en_core_web_sm")
def intent_ext(user_input):
	doc = nlp(user_input)
	dobj = ''
	tverb = ''
	for token in doc:
		if token.dep_ == 'dobj':
			dobj = token
			tverb = token.head
	# extract the verb for the intent's definition
	if tverb:
		intentVerb = ''
		verbList = ['create', 'want', 'like', 'need', 'order', 'place', 'make' ]
		if tverb.text in verbList:
			intentVerb = tverb
		else:
			if tverb.head.dep_ == 'ROOT':
				intentVerb = tverb.head
		# extract the object for the intent's definition
		intentObj = ''
		objList = ['pizza', 'cola']
		if dobj.text in objList:
			intentObj = dobj
		else:
			for child in dobj.children:
				if child.dep_ == 'prep':
					intentObj = list(child.children)[0]
					break
				elif child.dep_ == 'compound':
					intentObj = child
					break
		if intentObj:
			# print the intent expressed in the sample sentence
			return intentVerb.text + intentObj.text.capitalize()
	return user_input
