import sys
from wit import Wit

#if len(sys.argv) != 2:
#    print('usage: python ' + sys.argv[0] + ' <wit-token>')
#    exit(1)
access_token = "IZ77A6RNONUWCXFJVPTPP4SMKXGWCR5V"

# Quickstart example
# See https://wit.ai/ar7hur/Quickstart

def first_entity_value(entities, entity):
    if entity not in entities:
        return None
    val = entities[entity][0]['value']
    if not val:
        return None
    return val['value'] if isinstance(val, dict) else val

def send(request, response):
    print(response['text'])

def get_forecast(request):
    context = request['context']
    entities = request['entities']
    #print(first_entity_value(entities, 'intent'))
    loc = first_entity_value(entities, 'location')
    if loc:
        context['forecast'] = 'sunny'
    else:
        DRP = first_entity_value(entities, 'intent')
        if DRP == 'CloseConversation':
            context['DropIt'] = True
            context['missingLocation'] = False
            if context.get('forecast') is not None:
                del context['forecast']

        else:
            context['missingLocation'] = True
            if context.get('forecast') is not None:
                del context['forecast']

    return context

def get_joke(request):
    context = request['context']
    entities = request['entities']

    context['Joke'] = 'lalalalalalala'

    return context

actions = {
    'send': send,
    'getForecast': get_forecast,
    'getJoke': get_joke,
}

client = Wit(access_token=access_token, actions=actions)
client.interactive()
