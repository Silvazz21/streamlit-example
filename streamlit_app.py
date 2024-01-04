import streamlit as st
import itertools

def find_combinations(numbers, target):
    try:
        number_list = [float(i.replace(',', '.')) for i in numbers.split('\n') if i.strip()]
        target_value = float(target.replace(',', '.'))
        number_list = [int(x * 100) for x in number_list]
        target_list = int(target_value * 100)
        result = [seq for i in range(len(number_list), 0, -1)
                  for seq in itertools.combinations(number_list, i)
                  if sum(seq) == target_list]
        result_list = [tuple(x / 100.0 for x in tpl) for tpl in result]
        return result_list
    except ValueError:
        return None

def format_results(results):
    formatted_results = ""
    for combination in results:
        formatted_results += ", ".join([f"{num:.2f}" for num in combination]) + "\n"
    return formatted_results

def main():
    st.title("Combinações - Doc's Conta Corrente")

    st.write("Inserir os números separados por linha.")
    
    numbers_input = st.text_area("Inserir os números aqui (diretamente do excel, ou um por linha, separados por um Enter,)")
    target_input = st.text_input("Valor a procurar")

    if st.button("Encontrar combinações"):
        if numbers_input.strip() == "" or target_input.strip() == "":
            st.warning("Por favor insira os números e o valor a procuar.")
        else:
            result_list = find_combinations(numbers_input, target_input)
            if result_list is not None and len(result_list) > 0:
                st.write("Result:")
                formatted_results = format_results(result_list)
                st.text_area("Combinações", value=formatted_results, height=200)
            else:
                st.warning("Erro: Assegure que os números estão bem formatados, e que o resultado é atingível.")

if __name__ == "__main__":
    main()
