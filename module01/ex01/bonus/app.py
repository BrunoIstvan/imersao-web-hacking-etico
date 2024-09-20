import xml.etree.ElementTree as ET
from defusedxml.ElementTree import fromstring

def validate_and_return_xml(xml_content):
    try:
        # Usando defusedxml para evitar XXE
        tree = fromstring(xml_content)
        # Se o XML for válido, retorna o conteúdo original
        return xml_content, True
    except ET.ParseError:
        return "XML inválido", False
    except Exception as e:
        return f"Erro ao processar XML: {e}", False

# Exemplo de uso
xml_inputs = [
"""<?xml version="1.0"?>
<data>
    <item>Exemplo</item>
</data>
"""
,
"""<?xml version="1.0"?>
<note>
  <to>Bruno</to>
  <from>Destinario</from>
  <heading>Aulas Vulnerabilidades</heading>
  <body>XXE</body>
</note>
"""
,
"""<?xml version="1.0"?>
<!DOCTYPE root [
    <!ELEMENT root ANY>
    <!ENTITY xxe SYSTEM 'file:///etc/passwd'>
]>
<root> &xxe; </root>
""",
"""
<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "http://internal.vulnerable-website.com/"> ]>
""",
"""
<?xml version="1.0" encoding="ISO-8859-1"?>
<!DOCTYPE foo
    [<!ELEMENT foo ANY >
    <!ENTITY xxe SYSTEM "expect://exec('ls -la')" >
]>
<creds>
  <user> &xxe; </user>
  <pass> 123 </pass>
</creds>
"""
]

contador = 1
for xml_input in xml_inputs:

    print(f'\n>>>>>>>>>>>>>>>>>>>>>>>> Teste {contador} >>>>>>>>>>>>>>>>>>>>>>>>\n')
    print(xml_input)
    resultado, valido = validate_and_return_xml(xml_input)
    print('##### Válido:', valido, '- Saída:\n', resultado)
    contador += 1


