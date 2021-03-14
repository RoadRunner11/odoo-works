import spacy

nlp = spacy.load("en_core_web_sm")

def details_to_str(user_data):
    details = list()
    for key, value in user_data.items():
        details.append('{} - {}'.format(key, value))
    return "\n".join(details).join(['\n', '\n'])

def intent_ext(user_input):
	#Here should be the code created as suggested in the Expanding the Chatbot section earlier
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
        createList = ['create', 'place', 'make' ]
        getList = ['get', 'want', 'like', 'need', ]
        if tverb.text in createList + getList:
            intentVerb = tverb
        else:
            if tverb.head.dep_ == 'ROOT':
                intentVerb = tverb.head
        # extract the object for the intent's definition
        intentObj = ''
        objList = ['sale', 'order', 'quotation']
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
        
        if intentVerb.text in createList:
            # print the intent expressed in the sample sentence
            verb = 'create'
#             print(intentVerb.text + intentObj.text.capitalize())
            if intentObj.text in objList:
                obj = 'Sale'
                return verb+obj
            return "do you want to create a sale order?"
        if intentVerb.text in getList:
            verb = 'get'
            if intentObj.text in objList:
                obj = 'Sale'
                return verb+obj
            return "do you want to get a sale order?"
    return 'Please rephrase your request. Be as specific as possible!'

# def int_ext(inp):
#     intent = extract_intent(inp)
#     if intent == 'createSale':
#         context = {"name":'', 'partner_id': "", 'pricelist_id':"" }
#         print('We need some more information to place create sale.')
#         return add_sale_info(context) 
#     elif intent == 'getSale':
#         input('Would you like to get a sale record?')
#     else:
#         input('Your intent is not recognized.')
#     return input('Please rephrase your request. Be as specific as possible!') 

def add_sale_info(inp, context):
    doc = nlp(msg)
    ids = []
    for token in doc:
        if token.pos_ == 'NOUN':
            context['name'] = token.text
        elif token.pos_ == 'NUM':
            ids.append(token.text)
    if context.values():
        context['partner_id'], context['pricelist_id'] = ids[0], ids[1]
		return _("Your sale has been created." "{}" "Have a nice day!".format(details_to_str(context)))
    else:
        return _("Cannot extract necessary info. Please try again.")
