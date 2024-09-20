import base64
import pickle
import sys


commands = ['cat /etc/passwd', 'echo "Bla bla bla" > teste2.log; ls -la; cat teste2.log' ]


for com in commands:
    pickle_dumps = pickle.dumps(com)
    base64_hash = base64.urlsafe_b64encode(pickle_dumps)

    if sys.version_info[0] < 3:    
        str_data = str(base64_hash)
    else:
        str_data = str(base64_hash, encoding='UTF-8')

    print(str_data)



