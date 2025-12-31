from flask import Flask, request
from lxml import etree

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process_xml():
    xml_data = request.data
    
    # ✅ THE FIX: Explicitly Disable Features
    # We turn off network access and entity resolution.
    parser = etree.XMLParser(
        resolve_entities=False, # Don't resolve &name;
        no_network=True,        # Don't fetch URLs
        dtd_validation=False    # Don't process DTDs
    )
    
    try:
        tree = etree.fromstring(xml_data, parser)
        content = tree.find('text').text
        return f"Parsed Content: {content}"
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(debug=True, port=5005)