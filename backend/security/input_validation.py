from urllib.parse import urlparse
import re

max_url_length = 2048

def validate_url(url):
    
    if not url:
        return False, "URL não pode ser vazio"
    
    if not isinstance(url, str):
        return False, "Formato invalido: URL deve ser uma string"
    
    url = url.strip()

    if len(url) > max_url_length:
        return False, "URL excede tamanh9o máximo permitido"
    
    if not url.startswith(("http://", "https://")):
        return False, "URL deve começar com http:// ou https://"
    
    parsed = urlparse(url)

    if not parsed.netloc:
        return False, "Estrutura de URL Inválida"
    
    if re.search(r"[<>\"'{}|\\^`]", url):
        return False, "URL contém caracteres inválidos"
    
    return True, url