import numpy as np
from fuzzywuzzy import fuzz, process

# Base de Conocimientos: Definicion de reglas y criterios de clasificacion
def define_rules():
    rules = {
        "accion": ["ritmo rapido", "combate", "aventura"],
        "estrategia": ["planificacion", "tacticas", "gestion de recursos"],
        "rompecabezas": ["resolucion de problemas", "logica", "acertijos"],
        "simulacion": ["realista", "simulacion", "vida real"],
        "deporte": ["ritmo rapido", "competencia", "habilidad"],
        "cooperativo": ["cooperativo", "trabajo en equipo", "multijugador", "multijugador local"]
    }
    return rules

# Base de Hechos: Datos sobre videojuegos
def define_facts():
    facts = {
        "fortnite": ["ritmo rapido", "combate", "accion", "multijugador"],
        "jurassic world": ["planificacion", "gestion de recursos"],
        "sims": ["planificacion", "simulacion"],
        "sims4": ["planificacion", "simulacion", "realista"],
        "battlefield": ["resolucion de problemas", "logica", "combate", "multijugador"],
        "call of duty": ["ritmo rapido", "combate", "accion", "multijugador"],
        "civilization vi": ["planificacion", "tacticas", "gestion de recursos"],
        "portal": ["resolucion de problemas", "logica", "acertijos"],
        "flight simulator": ["realista", "simulacion", "vida real"],
        "overwatch": ["ritmo rapido", "combate", "accion", "multijugador"],
        "age of empires": ["planificacion", "tacticas", "gestion de recursos"],
        "tetris": ["resolucion de problemas", "logica", "acertijos"],
        "simcity": ["planificacion", "gestion de recursos", "simulacion"],
        "minecraft": ["aventura", "creatividad", "supervivencia", "multijugador"],
        "stardew valley": ["planificacion", "gestion de recursos", "simulacion"],
        "kerbal space program": ["realista", "simulacion", "planificacion"],
        "assassin's creed": ["aventura", "combate", "accion"],
        "command & conquer": ["planificacion", "tacticas", "gestion de recursos"],
        "the witness": ["resolucion de problemas", "logica", "acertijos"],
        "cities: skylines": ["planificacion", "gestion de recursos", "simulacion"],
        "red dead redemption": ["aventura", "combate", "accion"],
        "starcraft": ["planificacion", "tacticas", "gestion de recursos"],
        "candy crush": ["resolucion de problemas", "logica", "acertijos"],
        "farming simulator": ["realista", "simulacion", "gestion de recursos"],
        "grand theft auto": ["aventura", "accion", "combate"],
        "total war": ["planificacion", "tacticas", "gestion de recursos"],
        "monument valley": ["resolucion de problemas", "logica", "acertijos"],
        "euro truck simulator": ["realista", "simulacion", "vida real"],
        "doom": ["ritmo rapido", "combate", "accion"],
        "company of heroes": ["planificacion", "tacticas", "gestion de recursos"],
        "baba is you": ["resolucion de problemas", "logica", "acertijos"],
        "rollercoaster tycoon": ["planificacion", "gestion de recursos", "simulacion"],
        "rocket league": ["ritmo rapido", "deporte", "accion", "multijugador", "multijugador local","estrategia"],
        "overcooked 2": ["cooperativo", "estrategia", "gestion de recursos", "multijugador", "multijugador local"]
    }
    return facts

# Motor de Inferencia: Evaluar reglas y hechos para hacer recomendaciones
def infer(preferences, rules, facts):
    recomendaciones = []
    justificacion = []
    
    for game, features in facts.items():
        for preference in preferences:
            match_ratio = fuzz.token_set_ratio(preference, " ".join(features))
            if match_ratio > 80:  # Umbral de coincidencia
                recomendaciones.append(game)
                justificacion.append(f"El juego '{game}' coincide con la preferencia '{preference}' con una relación de coincidencia de {match_ratio}%.")
                break
    
    return recomendaciones, justificacion

# Subsistema de Justificación: Explicar las recomendaciones
def print_justificacion(justificacion):
    print("Justificaciones de las recomendaciones:")
    for justification in justificacion:
        print(f"- {justification}")

# Recomendación de Videojuegos: Encuentra juegos similares basados en las preferencias del usuario
def recommend_games(preferences, rules, facts):
    recomendaciones, justificacion = infer(preferences, rules, facts)
    return recomendaciones, justificacion

def main():
    # Definir reglas y hechos
    rules = define_rules()
    facts = define_facts()

    # Imprimir las reglas
    print("Ingrese sus preferencias de videojuegos basadas en las siguientes reglas:")
    for genre, criteria in rules.items():
        print(f"***************{genre.capitalize()}: {', '.join(criteria)}*************")

    while True:
        # Solicitar preferencias del usuario
        user_preferences = input("*******Ingrese sus preferencias de videojuegos (separadas por comas) o 'termine' para salir: ******  ").lower()
        
        if user_preferences == "termine":
            print("Gracias por utilizar el sistema de recomendación de videojuegos.")
            break
        
        user_preferences = user_preferences.split(", ")
        
        # Recomendar videojuegos basados en las preferencias del usuario
        recomendaciones, justificacion = recommend_games(user_preferences, rules, facts)
        
        if recomendaciones:
            print("Basado en sus preferencias, podría gustarle jugar a los siguientes juegos:")
            for game in recomendaciones:
                print(f"- {game}")
            print_justificacion(justificacion)
        else:
            print("Lo siento, no se encontraron juegos que coincidan con sus preferencias.")

if __name__ == "__main__":
    main()
