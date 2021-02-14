from purviewcli.model import PurviewClassificationDef

def typedefsReadBusinessmetadatadef(args):
  typeDefKey = 'guid' if args['--name'] is None else 'name'
  typeDefVal = args['--guid'][0] if args['--name'] is None else args['--name']
  endpoint = '/api/atlas/v2/types/Businessmetadatadef/%s/%s' % (typeDefKey,typeDefVal)
  data = self.http_get(app='catalog', method='GET', endpoint=endpoint, params=None, payload=None)
  return data

def typedefsReadClassificationdef(args):
  typeDefKey = 'guid' if args['--name'] is None else 'name'
  typeDefVal = args['--guid'][0] if args['--name'] is None else args['--name']
  endpoint = '/api/atlas/v2/types/classificationdef/%s/%s' % (typeDefKey,typeDefVal)
  data = self.http_get(app='catalog', method='GET', endpoint=endpoint, params=None, payload=None)
  return data

def typedefsCreateClassificationdefs(args):
  endpoint = '/api/atlas/v2/types/typedefs'
  payload = {
    'classificationDefs': []
  }
  for classificationDef in args['--defName']:
    instance = PurviewClassificationDef(name=classificationDef)
    payload['classificationDefs'].append(instance.__dict__)
  data = self.http_get(app='catalog', method='POST', endpoint=endpoint, params=None, payload=payload)
  return data

def typedefsDeleteClassificationdef(args):
  endpoint = '/api/atlas/v2/types/typedefs'
  classification = getClassificationdef({
    '--guid': args.get('--guid'),
    '--name': args.get('--name')
  })
  payload = {'classificationDefs': []}
  payload['classificationDefs'].append(classification)
  data = self.http_get(app='catalog', method='DELETE', endpoint=endpoint, params=None, payload=payload)
  return data

def typedefsUpdateClassificationdefs(args):
  endpoint = '/api/atlas/v2/types/typedefs'
  payload = {
    'classificationDefs': []
  }
  count = len(args['--defName'])
  for x in range(0,count):
    classification = getClassificationdef({
      '--name': args['--defName'][x]
    })
    classification['description'] = args['--defDescription'][x] if len(args['--defDescription']) > x else classification['description']
    classification['options']['displayName'] = args['--defDisplayName'][x] if len(args['--defDisplayName']) > x else classification['options']['displayName']
    payload['classificationDefs'].append(classification)
  data = self.http_get(app='catalog', method='PUT', endpoint=endpoint, params=None, payload=payload)
  return data
  
def typedefsReadEntitydef(args):
  typeDefKey = 'guid' if args['--name'] is None else 'name'
  typeDefVal = args['--guid'][0] if args['--name'] is None else args['--name']
  endpoint = '/api/atlas/v2/types/entitydef/%s/%s' % (typeDefKey,typeDefVal)
  data = self.http_get(app='catalog', method='GET', endpoint=endpoint, params=None, payload=None)
  return data

def typedefsReadEnumdef(args):
  typeDefKey = 'guid' if args['--name'] is None else 'name'
  typeDefVal = args['--guid'][0] if args['--name'] is None else args['--name']
  endpoint = '/api/atlas/v2/types/enumdef/%s/%s' % (typeDefKey,typeDefVal)
  data = self.http_get(app='catalog', method='GET', endpoint=endpoint, params=None, payload=None)
  return data

def typedefsReadRelationshipdef(args):
  typeDefKey = 'guid' if args['--name'] is None else 'name'
  typeDefVal = args['--guid'][0] if args['--name'] is None else args['--name']
  endpoint = '/api/atlas/v2/types/relationshipdef/%s/%s' % (typeDefKey,typeDefVal)
  data = self.http_get(app='catalog', method='GET', endpoint=endpoint, params=None, payload=None)
  return data

def typedefsReadStructdef(args):
  typeDefKey = 'guid' if args['--name'] is None else 'name'
  typeDefVal = args['--guid'][0] if args['--name'] is None else args['--name']
  endpoint = '/api/atlas/v2/types/structdef/%s/%s' % (typeDefKey,typeDefVal)
  data = self.http_get(app='catalog', method='GET', endpoint=endpoint, params=None, payload=None)
  return data

def typedefsReadTypedef(args):
  typeDefKey = 'guid' if args['--name'] is None else 'name'
  typeDefVal = args['--guid'][0] if args['--name'] is None else args['--name']
  endpoint = '/api/atlas/v2/types/Typedef/%s/%s' % (typeDefKey,typeDefVal)
  data = self.http_get(app='catalog', method='GET', endpoint=endpoint, params=None, payload=None)
  return data

def typedefsDeleteTypedefName(args):
  endpoint = '/api/atlas/v2/types/typedef/name/%s' % args['--name']
  data = self.http_get(app='catalog', method='DELETE', endpoint=endpoint, params=None, payload=None)
  return data

def typedefsRead(args):
  endpoint = '/api/atlas/v2/types/typedefs'
  params = {'type': args['--type']} if args['--type'] else None
  data = self.http_get(app='catalog', method='GET', endpoint=endpoint, params=params, payload=None)
  return data

def typedefsReadHeaders(args):
  endpoint = '/api/atlas/v2/types/typedefs/headers'
  data = self.http_get(app='catalog', method='GET', endpoint=endpoint, params=None, payload=None)
  return data
