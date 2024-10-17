import http.server
import socketserver
import xml.etree.ElementTree as ET

class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        # Parseia o XML
        root = ET.fromstring(post_data)

        # Lê os parâmetros do XML
        try:
            # Busca pelos valores em sequência
            params = root.findall('.//param/value')

            # Verificar se todos os parâmetros foram encontrados
            if len(params) != 4:
                raise ValueError("Número incorreto de parâmetros")

            nome = params[0].find('string').text
            nivel = params[1].find('string').text
            salario_bruto = float(params[2].find('double').text)
            dependentes = int(params[3].find('int').text)

            # Calcular o desconto
            if nivel == "A":
                desconto = 0.03 if dependentes == 0 else 0.08
            elif nivel == "B":
                desconto = 0.05 if dependentes == 0 else 0.10
            elif nivel == "C":
                desconto = 0.08 if dependentes == 0 else 0.15
            elif nivel == "D":
                desconto = 0.10 if dependentes == 0 else 0.17
            else:
                self.send_response(400)
                self.send_header('Content-Type', 'text/xml')
                self.end_headers()
                invalid_level_response = """<?xml version="1.0"?>
<methodResponse>
    <fault>
        <value>
            <struct>
                <member>
                    <name>faultCode</name>
                    <value><int>2</int></value>
                </member>
                <member>
                    <name>faultString</name>
                    <value><string>Nível inválido</string></value>
                </member>
            </struct>
        </value>
    </fault>
</methodResponse>"""
                self.wfile.write(invalid_level_response.encode('utf-8'))
                return

            # Cálculo do salário líquido
            salario_liquido = salario_bruto * (1 - desconto)

            # Preparar resposta
            self.send_response(200)
            self.send_header('Content-Type', 'text/xml')
            self.end_headers()
            response = f"""<?xml version="1.0"?>
<methodResponse>
    <params>
        <param>
            <value>
                <struct>
                    <member>
                        <name>nome</name>
                        <value><string>{nome}</string></value>
                    </member>
                    <member>
                        <name>nivel</name>
                        <value><string>{nivel}</string></value>
                    </member>
                    <member>
                        <name>salario_liquido</name>
                        <value><double>{salario_liquido:.2f}</double></value>
                    </member>
                </struct>
            </value>
        </param>
    </params>
</methodResponse>"""

            self.wfile.write(response.encode('utf-8'))

        except Exception as e:
            self.send_response(400)
            self.send_header('Content-Type', 'text/xml')
            self.end_headers()
            error_response = f"""<?xml version="1.0"?>
<methodResponse>
    <fault>
        <value>
            <struct>
                <member>
                    <name>faultCode</name>
                    <value><int>1</int></value>
                </member>
                <member>
                    <name>faultString</name>
                    <value><string>{str(e)}</string></value>
                </member>
            </struct>
        </value>
    </fault>
</methodResponse>"""
            self.wfile.write(error_response.encode('utf-8'))

# Configurações do servidor
PORT = 8000
Handler = MyRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Servidor rodando na porta", PORT)
    httpd.serve_forever()
