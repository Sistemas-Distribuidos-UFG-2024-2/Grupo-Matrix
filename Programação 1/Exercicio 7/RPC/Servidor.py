from http.server import BaseHTTPRequestHandler, HTTPServer
import xml.etree.ElementTree as ET

class MyRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        # Processar a requisição XML
        try:
            root = ET.fromstring(post_data)
            method_name = root.find('methodName').text

            if method_name == "pode_aposentar":
                # Encontrar os parâmetros corretamente
                params = root.find('params')
                idade = int(params[0].find('value/int').text)
                tempo_servico = int(params[1].find('value/int').text)

                pode_aposentar = self.verifica_aposentadoria(idade, tempo_servico)

                response = f"""<?xml version='1.0'?>
                <methodResponse>
                    <params>
                        <param>
                            <value><boolean>{str(pode_aposentar).lower()}</boolean></value>
                        </param>
                    </params>
                </methodResponse>"""

                self.send_response(200)
                self.send_header('Content-Type', 'text/xml')
                self.send_header('Content-Length', str(len(response)))
                self.end_headers()
                self.wfile.write(response.encode('utf-8'))

        except ET.ParseError as e:
            self.send_error(400, f"Parse error: {str(e)}")
        except Exception as e:
            self.send_error(500, f"Internal server error: {str(e)}")

    def verifica_aposentadoria(self, idade, tempo_servico):
        if idade >= 65 or tempo_servico >= 30 or (idade >= 60 and tempo_servico >= 25):
            return True
        return False

def run(server_class=HTTPServer, handler_class=MyRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Servidor rodando na porta {port}...')
    httpd.serve_forever()

if __name__ == "__main__":
    run()
