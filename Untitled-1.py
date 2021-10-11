from dataclasses import dataclass

@dataclass
class TypeOfMainAssets:
    code: int
    type: str

    @dataclass
    class MoveofMainAssets:
        name: str
        code: int
        remainder: float
        received:float
        output: float

type_array = []
type_array.append(TypeOfMainAssets(10,"Яловичина"))
type_array.append(TypeOfMainAssets(20,"Свинина"))
type_array.append(TypeOfMainAssets(30,"Сало"))

move_array = []
move_array.append(MoveOfMainAssets("серпень",25.5, 23.5, 30.8, 23.7))
move_array.append(MoveOfMainAssets("серпень",25.0, 25.5, 25.5, 25.7))
move_array.append(MoveOfMainAssets("серпень",14.4, 14.5, 14.5, 14.5))
move_array.append(MoveOfMainAssets("вересень",23.5, 24.0, 24.0, 24.5))
move_array.append(MoveOfMainAssets("вересень",25.5, 26.0, 26.3, 26.5))
move_array.append(MoveOfMainAssets("вересень",14.5, 14.6, 14.8, 15.0))
move_array.append(MoveOfMainAssets("жовтень",25.0, 25.0, 25.5, 25.5))
move_array.append(MoveOfMainAssets("жовтень",26.6, 26.8, 27.0, 27.4))
move_array.append(MoveOfMainAssets("жовтень",15.5, 15.5, 15.6, 16.0))

def printMoveOfMainAssets(moveOfMainAssets):
    '''printMoveOfMainAssets function prints
    "Ринкові ціни на продукти по місяцях"
    with names and values'''

    print("Код: {code}, Тип: {type}"
          .format(code = typeofMainAssets.code, type=TypeOfMainAssets.type))

for data in type_array :
    printTypeOfMainAssets(data)

