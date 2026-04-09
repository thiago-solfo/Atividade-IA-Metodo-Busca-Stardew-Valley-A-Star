import sys
from astar import GRAPH, HEURISTIC, get_checkpoints, a_star_with_checkpoints

def main():
    log_path = 'testes_dias.log'
    
    with open(log_path, 'w', encoding='utf-8') as log_file:
        # Classe para duplicar a saída (mostra no console e salva no arquivo ao mesmo tempo)
        class DualLogger:
            def __init__(self, file, console):
                self.file = file
                self.console = console

            def write(self, message):
                self.console.write(message)
                self.file.write(message)

            def flush(self):
                self.console.flush()
                self.file.flush()
        
        
        original_stdout = sys.stdout
        sys.stdout = DualLogger(log_file, sys.stdout)
        
        try:
            print("=== Teste automatizado de todos os dias (1 a 29) ===\n")
            
            for dia in range(1, 30):
                print(f"--- TESTANDO DIA {dia} ---")
                
                # get_checkpoints já possui vários prints integrados, então eles também serão capturados e logados
                checkpoints = get_checkpoints(dia)
                print(f"Checkpoints (Lista): {checkpoints}")
                
                cost, path = a_star_with_checkpoints(
                    GRAPH,
                    'Casa',
                    'Praia',
                    checkpoints,
                    HEURISTIC
                )
                
                if cost == -1:
                    print("Nao achou caminho!")
                else:
                    print(f"Custo total: {cost} min")
                    print(f"Caminho: {' -> '.join(path)}")
                
                print("\n" + "="*40 + "\n")
                
        finally:
            # Restaura a saída padrão do sistema
            sys.stdout = original_stdout
            
    print(f"Testes finalizados! Resultados salvos no arquivo '{log_path}'.")

if __name__ == '__main__':
    main()