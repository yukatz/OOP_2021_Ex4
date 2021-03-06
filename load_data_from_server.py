import json
import networkx as nx
from Agent import Agent
from Position import Position
from Pokemon import Pokemon


def load_graph_json(graph_json):
    """load the graph from json string that we get from the server """
    j_graph = json.loads(graph_json)
    graph = nx.DiGraph()
    for i in j_graph["Nodes"]:
        graph.add_node(int(i["id"]), pos=Position(location=i["pos"]))
    for j in j_graph["Edges"]:
        graph.add_edge(int(j["src"]), int(j["dest"]), weight=float(j['w']))
    return graph


def load_agents_list(agents_json):
    """load all agents from json string that we get from the server into list """
    agents_list = []
    agents_json = json.loads(agents_json)
    x = len(agents_json['Agents'])
    for i in range(x):
        agents_list.append(Agent(agent_str=agents_json["Agents"][i]['Agent']))
    return agents_list


def load_pokemon_list(pokemon_json, graph: nx.DiGraph):
    """load all Pokemons from json string that we get from the server into list """
    pokemon_list = []
    pokemon_json = json.loads(pokemon_json)
    x = len(pokemon_json["Pokemons"])
    for i in range(x):
        pokemon_list.append(Pokemon(graph, json_pok=pokemon_json["Pokemons"][i]["Pokemon"]))
        pokemon_list.sort(key=lambda x: x.value, reverse=True)
    return pokemon_list
