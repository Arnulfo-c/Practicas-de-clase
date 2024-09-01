import nltk
from nltk.chat.util import Chat, reflections

# Definir pares de patrones y respuestas
pares = [
    [
        r"mi nombre es (.*)",
        ["Hola %1, ¿En que podemos ayudarte?",]
    ],
    [
        r"Cuales son los cursos disponibles?",
        ["Ofrecemos programas en Ingeniería, Ciencias Sociales, Artes y más.",]
    ],
    [
        r"Como puedo ingresar a la universidad",
        ["Puedes inscribirte a través de nuestro sitio web o visitando la oficina de admisiones.",]
    ],
    [
        r"como son los requisitos para ingresar",
        ["Los requisitos varían según el programa, pero generalmente incluyen un formulario de solicitud, transcripciones académicas y una carta de motivación.",]
    ],
    [
        r"Hasta pronto",
        ["¡Adiós! Si tienes más preguntas, no dudes en preguntar.",]
    ],
]

# Crear una instancia del chatbot
chatbot = Chat(pares, reflections)

# Función para iniciar el chatbot
def iniciar_chatbot():
    print("¡Hola! Esta es la universidad de Oriente Univo. ¿En qué puedo ayudarte?")
    chatbot.converse()

# Iniciar el chatbot
if __name__ == "__main__":
    iniciar_chatbot()
