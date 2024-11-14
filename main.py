from banco.banco import main
from jsonschema import validate
from banco.input_validation.input_schema import schema

import json
import os
from pathlib import Path

def read_input(input_path)->str:
    """
        import a json file and reads its content
    """

    with open(input_path, encoding="utf-8") as input_model:
        input_data = json.load(input_model)

    return input_data

def get_input_dir() -> str:
    """
        return the directory of input_model.json
    """

    basic_file = 'input_model.json'

    input_dir = "input_model"

    all_dir = os.listdir()

    if input_dir not in all_dir:
        raise Exception("The directory input_model is not in basic directory")

    project_path = str(Path.cwd())

    input_path = project_path + "/" + input_dir + "/" + basic_file

    return input_path

def main_menu(input_data):
    """
        Simple menu that directs the user mode
    """

    print("Por favor, indique se quer entrar no aplicativo como gerente ou usuário de terminal eletrônico\n")
    print("1 para gerente ou 2 para usuário")

    mode = int(input())

    if mode == 1:
        print("Modo gerente")
    elif mode == 2:
        main(input_data=input_data)
    else:
        print("Opção não encontrada")
        main_menu(input_data=input_data)


if __name__ == '__main__':


    input_path = get_input_dir()
    input_data = read_input(input_path=input_path)

    validate(instance=input_data, schema=schema)

    main_menu(input_data=input_data)
