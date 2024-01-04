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

def main():
    st.title("Find Combinations App")

    st.write("Enter numbers separated by newlines and specify the target value.")
    
    numbers_input = st.text_area("Enter numbers here (one per line)")
    target_input = st.text_input("Enter the target value")

    if st.button("Find Combinations"):
        if numbers_input.strip() == "" or target_input.strip() == "":
            st.warning("Please enter numbers and a target value.")
        else:
            result_list = find_combinations(numbers_input, target_input)
            if result_list is not None and len(result_list) > 0:
                st.write("Result:")
                st.write(result_list)
            else:
                st.warning("Error: Ensure numbers are properly formatted and target value is achievable.")

if __name__ == "__main__":
    main()
