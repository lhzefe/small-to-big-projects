print(r"""
                            _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
              _.-:'_.-::::::'  ||
            .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
          ||   ||::::::'     _.;._'-._
          ||   ||:::::'  _.-!oo @.!-._'-.
          \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
              ||-._'-.@.-'_.-' _.-o  |'||
              ||=[ '-._.-\U/.-'    o |'||
              || '-.]=|| |'|      o  |'||
              ||      || |'|        _| ';
              ||      || |'|    _.-'_.-'
              |'-._   || |'|_.-'_.-'
                '-._'-.|| |' `_.-'
                    '-.||_/.-'
      """)
print("Welcome to Treasure Island.Your mission is to find the treasure.")
way = input("Choose to go 'left' or 'right': ")
if way.lower() == "left":
    way = input("Choose to 'swim' or 'wait': " )
    if way.lower() == "wait":
        way = input("Which door? 'red', 'blue' or 'yellow'? ")
        if way.lower() == "red":
            print("Burned by fire. Game Over.")
        elif way.lower() == "blue":
            print("Eaten by beasts. Game Over.")
        elif way.lower() == "yellow":
            print("You Win!")
        else:
            print("Game Over.")
    else:
        print("Attacked by trout. Game Over.")
else:
    print("Fall into a hole. Game Over.")
