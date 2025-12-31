from flask import Flask, request
from lxml import etree

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process_xml():
    xml_data = request.data
    
    # 🛑 THE VULNERABILITY:
    # The XML parser is initialized with default settings that allow
    # resolving external entities (like file paths or URLs).
    parser = etree.XMLParser(resolve_entities=True)
    
    try:
        tree = etree.fromstring(xml_data, parser)
        content = tree.find('text').text
        return f"Parsed Content: {content}"
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(debug=True, port=5005)