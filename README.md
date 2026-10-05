1. Componentes Básicos y Metacarácteres
Estas son las piezas fundamentales para construir cualquier patrón de búsqueda.
• ^ — Inicio de cadena: Coincide con el comienzo del texto. re.match(r'^Hola', texto)
• $ — Fin de cadena: Coincide con el final del texto. re.search(r'adiós$', texto)
• . — Cualquier carácter: Coincide con cualquier símbolo excepto el salto de línea.
• * — Cero o más veces: Multiplica el elemento anterior de 0 a infinitas veces.
• + — Una o más veces: Multiplica el elemento anterior mínimo 1 vez.
• ? — Cero o una vez / Opcional: Hace que el elemento anterior sea opcional.
• | — Operador O (OR): Coincide con el patrón de la izquierda o de la derecha. r'gato|perro'
• \ — Escape: Convierte un metacarácter en un carácter literal. r'\.' busca un punto real.
2. Clases de Caracteres Predefinidas
Símbolos rápidos para representar grupos enteros de letras, números o espacios.
• \d — Cualquier dígito: Equivale a [0-9].
• \D — Cualquier no-dígito: Coincide con letras, espacios o símbolos (todo menos números).
• \w — Carácter alfanumérico: Letras, números y guion bajo _. Equivale a [a-zA-Z0-9_].
• \W — Carácter no alfanumérico: Signos de puntuación, espacios, etc.
• \s — Espacio en blanco: Coincide con espacios, tabulaciones (\t) y saltos de línea (\n).
• \S — Cualquier carácter que no sea espacio.
• \b — Límite de palabra: Coincide con el inicio o fin de una palabra exacta. r'\bpan\b' no coincidirá con "pantalla".
• \B — No límite de palabra: Coincide si el patrón está dentro de otra palabra.
3. Rangos, Cuantificadores y Grupos
Herramientas para definir conjuntos exactos y repeticiones específicas.
• [a-z] — Letras minúsculas: Coincide con cualquier letra de la 'a' a la 'z'.
• [A-Z] — Letras mayúsculas: Coincide con cualquier letra de la 'A' a la 'Z'.
• [0-9] — Rango numérico: Exactamente igual a \d.
• [^0-9] — Negación: Coincide con cualquier cosa que no sea un número.
• {n} — Cantidad exacta: Se repite exactamente n veces. r'\d{4}' busca 4 números seguidos.
• {n,} — Cantidad mínima: Se repite n o más veces.
• {n,m} — Rango de cantidades: Se repite entre n y m veces. r'\w{2,5}'
• (...) — Grupo de captura: Agrupa caracteres para extraerlos juntos o aplicarles cuantificadores.
• (?:...) — Grupo de NO captura: Agrupa caracteres pero no los almacena en la memoria del resultado.
4. Patrones Prácticos para Validar Datos comunes
Fórmulas regex listas para producción en tus scripts de Python.
• ^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$ — Validar Correo Electrónico.
• ^\d{4}-\d{2}-\d{2}$ — Fecha en formato ISO (AAAA-MM-DD).
• ^(https?:\/\/)?([\da-z.-]+)\.([a-z.]{2,6})([\/\w .-]*)*\/?$ — Validar una URL / Link.
• ^\+?[\d\s-]{10,15}$ — Número de teléfono internacional.
• ^\d{5}$ — Código postal estándar (5 dígitos).
• ^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$ — Dirección IP (IPv4).
• ^#?([a-fA-F0-9]{6}|[a-fA-F0-9]{3})$ — Código de color Hexadecimal (ej: #FF5733).
• ^\d+$ — Validar si un texto contiene SOLO números.
• ^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$ — Validar nombres solo con letras y acentos españoles.
5. Métodos Clave del Módulo re en Python
6. https://gist.github.com/kevindiuss/8bc494fd2410392b5b281b1f5855f728
Cómo aplicar las expresiones anteriores en tu código.
• re.search(patrón, texto) — Buscar coincidencia: Busca en todo el texto y devuelve la primera coincidencia que encuentre.
• re.match(patrón, texto) — Coincidencia al inicio: Busca el patrón únicamente al principio de la cadena.
• re.findall(patrón, texto) — Extraer todo: Devuelve una lista con todos los textos que coincidieron.
• re.finditer(patrón, texto) — Iterar coincidencias: Devuelve un iterador con objetos de coincidencia (ideal para textos gigantes).
• re.sub(patrón, reemplazo, texto) — Buscar y reemplazar: Cambia los textos que coincidan por un nuevo texto.
• re.split(patrón, texto) — Dividir texto: Rompe una cadena en una lista usando el patrón como separador.
