
"""
usage: pv [--version] [--help] <command> [<args>...]

options:
   -v, --version
   -h, --help
   

The most commonly used pv commands are:
   entity           Entities are a collection of attributes that model or represent a data asset.
   glossary         Vocabularies for business users.
   lineage          Helps you understand the source and impact of data and changes to data over time.
   relationship     Relationships describe connections between two entities.
   typedefs         A Type in Atlas is a definition of how a particular type of metadata objects are stored and accessed.
   scan             Azure Purview scan.
   insight          Azure Purview insights.
   search           Azure Purview advanced search.

See 'pv <command>' for more information on a specific command.

"""
import sys
import os
import json
import importlib
from docopt import docopt
from purviewcli import __version__
from purviewcli.client import PurviewClient

def main():
    args = docopt(__doc__, version=__version__, options_first=True)
    argv = [args['<command>']] + args['<args>']

    # Command
    command = args['<command>']
    if command in ['entity', 'relationship', 'lineage', 'glossary', 'typedefs', 'scan', 'insight', 'search']:
        globals()[command] = importlib.import_module('purviewcli.cli.' + command)
        command_args = docopt(eval(command).__doc__, argv=argv)
    else:
        exit("%r is not a purviewcli command." % args['<command>'])

    # Action
    action = None
    for item in command_args:
        if item[0] != '-' and item[0] != '<' and item != command and command_args[item] is True:
            action = item
    globals()['lib'] = importlib.import_module('purviewcli.client._' + command)

    # Method
    funcStr = command + action[0].upper() + action[1:]
    funcObj = eval('lib.' + funcStr)
    http_dict = funcObj(command_args)

    # Azure Purview client
    account_name = os.environ.get("PURVIEW_NAME")
    if account_name is None:
        print("[ERROR] Environment variable PURVIEW_NAME is missing. To set the environment variable, execute the following command: \033[94mexport PURVIEW_NAME=value\033[0m")
        sys.exit()
    client = PurviewClient(account_name=account_name)
    client.set_token()
    
    # Print data
    data = client.http_get(http_dict['app'], http_dict['method'], http_dict['endpoint'], http_dict['params'], http_dict['payload'])
    if len(data) > 0:
        print(json.dumps(data, indent=4, sort_keys=True)) 
    else:
        print('[INFO] No data found for %s.' % (command))

if __name__ == '__main__':
  main()
